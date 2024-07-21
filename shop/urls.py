
# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('upload/', views.product_upload, name='product_upload'),
]
