from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})

def cpanel_view(request, *args, **kwargs):
    return render(request, 'cpanel.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "page_name": "About Us",
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [1, 22, 5, 678]
    }
    print(request.user)
    return render(request, 'about.html', my_context)


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})