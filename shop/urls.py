
# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('index/', views.product_list, name='services'),
    path('index_api/', views.index_api, name='index_api'),
    path('index_admin/', views.index_admin, name='index_admin'),
    path('index_admin/user-mode.html', views.user_mode, name='user-mode'),
    path('index_shonbrunn/', views.index_shonbrunn, name='index_shonbrunn'),
    path('index_shonbrunn/user-mode.html', views.user_mode_shonbrunn, name='user_mode_shonbrunn'),
    path('index_hula/', views.index_hula, name='index_hula'),
    path('index_hula/user-mode.html', views.user_mode_hula, name='user_mode_hula'),
    path('create_order/', views.create_order, name='create_order'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('response/<int:pk>/', views.order_response, name='order_response'),  # New URL
    path('upload/', views.product_upload, name='product_upload'),
]
