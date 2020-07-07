from django.shortcuts import render

from .models import Product
from .forms import NewProductForm, RawProductForm
# Create your views here.


def product_create_view(request):
    form = NewProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewProductForm()

    context = {
        'form': form
    }
    return render(request, 'product/newproduct.html', context)
#
# def product_create_view(request):
#     prod_form = RawProductForm()
#     if request.method == "POST":
#         prod_form = RawProductForm(request.POST)
#         if prod_form.is_valid():
#             print(prod_form.cleaned_data)
#         else:
#             print(prod_form.errors)
#     context = {
#         'form': prod_form
#     }
#     return render(request, 'product/newproduct.html', context)


def product_inventory_view(request):
    inventory = Product.objects.all()
    context = {
        'inventory': inventory,
    }
    return render(request, 'inventory.html', context)


def product_detail_view(request, id):
    try:
        prod_id = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'product/productdetails.html', {'product':prod_id})

