
# shop/forms.py
from django import forms
from .models import Product
from .models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_address', 'order_details', 'uploaded_file']  # Include the new field
