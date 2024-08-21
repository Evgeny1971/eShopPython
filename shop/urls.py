
# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('index/', views.product_list, name='services'),
    path('create_order/', views.create_order, name='create_order'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('response/<int:pk>/', views.order_response, name='order_response'),  # New URL
    path('upload/', views.product_upload, name='product_upload'),
]
