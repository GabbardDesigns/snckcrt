import csv, io, json
from django.contrib import messages
from django.shortcuts import render
from .models import Product
from django.core.serializers.json import DjangoJSONEncoder
import logging


def product_select_items_view(request):
    inventory = Product.objects.order_by('title').exclude(active=False)
    context = {
        'inventory': inventory,
    }
    return render(request, 'selectItems.html', context)


def product_detail_view(request, id):
    try:
        inventory = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'product/productdetails.html', {'inventory': inventory, 'id':id})


def product_edit_view(request, id):
    try:
        prod_id = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'product/editproduct.html', {'product':prod_id})


def product_upload(request):
    # declaring template
    logging.info('Upload process started.')
    template = "product_upload.html"
    data = Product.objects.all()

# prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': '''Order of the CSV should be:
                    title: Must be test, no more than 20 characters
                    price: Must be a number
                    imagepath: You will ahve to edit the items to upload the images, so this can be anything but blank
                    alt: Alt image text: Free text with a 30 charcter limit
                    active: this is a boolean value and must be True or False
                    ''',
        'product': data
              }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    try:
        csv_file = request.FILES['file']
    except:
        messages.error(request, 'No file attached', 'Failed')
        return render(request, template, prompt)

    # check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE', 'Failed')
        return render(request, template, prompt)

    # checks file for parsability based on our schema
    try:
        data_set = csv_file.read().decode('UTF-8')
    except:
        messages.error(request, 'Please check the file, import error.', 'Failed')
        return render(request, template, prompt)

    # sets flag for plural text casing
    prodcount = 0
    plural= 's'

    # sets up stream that loops through each line
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Product.objects.update_or_create(
            title=column[0],
            price=column[1],
            imagepath=column[2],
            alt=column[3],
            active=column[4].title()
        )
        prodcount += 1
    if prodcount == 1:
        plural = ''

    context = {}

    #returns success messages
    messages.success(request, 'File uploaded successfully.', 'Success')
    messages.success(request, f'{prodcount} product{plural} added.', 'Success')

    # Force update of the json file for frontend
    inventory = Product.objects.order_by('title').exclude(active=False).values()
    with open('snckcrt/static/data/refund.json', 'w') as teacherfile:
        teacherfile.write('[')
        for count, product in enumerate(inventory):
            json.dump(product, teacherfile, cls=DjangoJSONEncoder)

            if count < len(inventory) - 1:
                teacherfile.write(', ')
        teacherfile.write(']')
        teacherfile.close()

    return render(request, template, context)

