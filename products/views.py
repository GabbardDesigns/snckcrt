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
