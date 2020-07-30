from django.urls import path
from products import views


urlpatterns = [
    # path('', views.product_select_items_view, name='index'),
    path('editproduct/<int:id>/', views.product_edit_view, name='editproducts'),
    path('selectproduct/', views.product_select_items_view, name='selectproduct'),
    path('details/<int:id>/', views.product_detail_view, name='viewdetails'),
]

