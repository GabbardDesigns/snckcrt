from django.urls import path, include
from users import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('', views.dashboard, name='dashboard'),
]
