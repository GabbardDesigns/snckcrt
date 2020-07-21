from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_select_items_view, name='index'),
    path('editproduct/', views.product_edit_view, name='editproducts'),
    path('selectproduct/', views.product_select_items_view, name='selectproduct'),
    path('details/<int:id>/', views.product_detail_view, name='viewdetails'),

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
