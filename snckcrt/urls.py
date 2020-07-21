"""snckcrt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static

from pages.views import home_view, contact_view, about_view, cpanel_view
from products.views import product_select_items_view


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('homes/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact_us'),
    path('inventory/', product_select_items_view, name='inventory'),
    path('product/', include('products.urls')),
    path('cpanel/', cpanel_view, name="control panel"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
