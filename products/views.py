import csv
import io
import json
import logging

from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from .models import Product


def product_select_items_view(request):
    """ defines the context and template to render the product detail select items url (product/selectProduct/)

       Returns:
            request: request object that requested this response
            template: product_upload.html - the page that this function will be called from
            context: inventory -  the QuerySet of all product information, filtered to exclude
                     inactive items and sorted alphabetically by title.
    """

    inventory = Product.objects.order_by('title').exclude(active=False)

    template = 'selectItems.html'
    context = {
        'inventory': inventory,
    }

    return render(request, template, context)


def product_detail_view(request, id):
    """ defines the context and template to render the product detail section on url (product/selectProduct/)

       Parameters:
            request: request object that requested this response
            id: int value passed in from the url that invokes the view
       Returns:
           template: product/productDetails.html - the page that this function will be called from
           context: inventory -  the QuerySet of information for the specific product requested
                                 using the id values passed in
                    id - returns the the id value that was passed in
    """
    try:
        inventory = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")

    template = 'product/productDetails.html'
    context = {
        'inventory': inventory,
        'id': id,
    }
    return render(request, template, context)


def product_edit_view(request, id):
    """ defines the context and template to redender the product edit url (product/editproduct/<int:id>/)

       Parameters:
            request: request object that requested this response
            id: request object that requested this response
       Returns:
           template: product/editProduct.html - the page that this function will be called from
           context: prod_info -  the QuerySet of information for the specific product requested
                    using the id values passed in
    """
    try:
        prod_info = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")

    template = 'product/editProduct.html'
    context = {
        'product': prod_info
    }

    return render(request, template, context)


def write_json(inventory):
    with open('snckcrt/static/data/inventory.json', 'w') as teacherfile:
        teacherfile.write('[')
        for count, product in enumerate(inventory):
            json.dump(product, teacherfile, cls=DjangoJSONEncoder)

            if count < len(inventory) - 1:
                teacherfile.write(', ')
        teacherfile.write(']')
        teacherfile.close()


def product_upload(request):
    """ defines the context and functionality for taking in a file,

       Parameters:
           request: request object that requested this response
       Returns:
           request: request object that requested this response
           template: product_upload.html - the page that this function will be called from
           context: prompt is the context variable, containing the messaging text for the rendered template.
    """

    # declaring template
    logging.info('Upload process started.')
    template = "product_upload.html"
    data = Product.objects.all()

    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': '''Order of the CSV should be:
                    title: Must be test, no more than 20 characters
                    price: Must be a number
                    imagepath: You will have to edit the items to upload the images, so this can be anything but blank
                    alt: Alt image text: Free text with a 30 character limit
                    active: this is a boolean value and must be True or False
                    ''',
        'product': data
    }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    # Error handling for file import
    try:
        csv_file = request.FILES['file']
    except MultiValueDictKeyError:
        messages.error(request, 'No file attached', 'Failed')
        return render(request, template, prompt)

    # check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, f'{csv_file.name.upper()} IS NOT A CSV FILE', 'Failed')
        return render(request, template, prompt)

    # checks file for parsability based on our schema
    try:
        data_set = csv_file.read().decode('UTF-8')
    except ImportError:
        messages.error(request, f'Import error with file {csv_file.name.upper()}. Please check the file and try again.',
                       'Failed')
        return render(request, template, prompt)

    # sets flag for plural text casing
    prodcount = 0
    plural = 's'

    # sets up stream that loops through each line
    io_string = io.StringIO(data_set)
    next(io_string)

    # validates against schema prior to attempt to create record.

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        try:
            if \
                    column[0] is str \
                    and column[1] is int or float \
                    and column[3] is str \
                    and column[4].title() is 'True' or 'False':

                    _, created = Product.objects.update_or_create(
                        title=column[0],
                        price=column[1],
                        imagepath=column[2],
                        alt=column[3],
                        active=column[4].title()
                    )
                    prodcount += 1
        except:
            messages.error(request,
                           f'''PARTIAL IMPORT ERROR:
                           Please check the file {csv_file.name.upper()}, an error occurred during parsing line {prodcount +1}
                           ''',
                           'Failed')

            # messages.error(request,
            #                f'',
            #                'Failed')
            return render(request, template, prompt)

    if prodcount == 1:
        plural = ''

    context = {}

    # returns success messages
    messages.success(request, f'File {csv_file.name.upper()} uploaded successfully.', 'Success')
    messages.success(request, f'{prodcount} product record{plural} updated or created.', 'Success')

    # Force update of the json file for frontend
    inventory = Product.objects.order_by('title').exclude(active=False).values()
    write_json(inventory)
    return render(request, template, context)
