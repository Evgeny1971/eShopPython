
# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from .forms import OrderForm


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

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)  # Include request.FILES to handle file upload
        if form.is_valid():
            order = form.save()
            # order = form.save(commit=False)  # Do not commit immediately
            uploaded_file = request.FILES.get('uploaded_file')
            print(f"request.FILES: {request.FILES}")

            if uploaded_file:
                # Display file details for testing
                file_name = uploaded_file.name
                file_size = uploaded_file.size
                file_type = uploaded_file.content_type

                # Here you can print the details to the console or log them
                print(f"Uploaded File Name: {file_name}")
                print(f"Uploaded File Size: {file_size} bytes")
                print(f"Uploaded File Type: {file_type}")
                order_link = request.build_absolute_uri(f'/order/{order.id}/')
                send_mail(
                    'New Order Submitted',
                    f'An order has been submitted. View it here: {order_link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER,'vika.vinnikov@gmail.com'],  # Replace with the actual manufacturer's email
                )

                # return redirect('order_detail', pk=order.pk)
                return redirect('order_detail', pk=order.pk)
                # Save the order and redirect as usual
                # order.save()

    else:
        form = OrderForm()
    return render(request, 'shop/create_order.html', {'form': form})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'shop/order_detail.html', {'order': order})

def send_order_email(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_link = request.build_absolute_uri(f'/order/{order.id}/')

    # Send an email to the manufacturer
    send_mail(
        'Order Information',
        f'View the order details here: {order_link}',
        settings.DEFAULT_FROM_EMAIL,
        settings.EMAIL_HOST_USER,  # Replace with actual manufacturer email
    )
