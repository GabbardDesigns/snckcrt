from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_inventory_view, name='index'),
    path('newproduct/', views.product_create_view, name='addproducts'),
    path('details/<int:id>/', views.product_detail_view, name='viewdetails'),
]

