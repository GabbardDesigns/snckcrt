import csv, io
from django.contrib import messages
from django.shortcuts import render
from .models import Product


def product_select_items_view(request):
    inventory = Product.objects.all()
    context = {
        'inventory': inventory,
    }
    return render(request, 'selectItems.html', context)

def product_detail_view(request, id):
    try:
        prod_id = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'product/productdetails.html', {'product':prod_id})


def product_edit_view(request, id):
    try:
        prod_id = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'product/editproduct.html', {'product':prod_id})


def product_upload(request):
    # declaring template
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

    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Product.objects.update_or_create(
            title=column[0],
            price=column[1],
            imagepath=column[2],
            alt=column[3],
            active=column[4]
        )
    context = {}
    return render(request, template, context)