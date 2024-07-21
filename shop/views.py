
# shop/views.py
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'shop/product_list.html', {'products': products})

def product_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_upload.html', {'form': form})
