
# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.mail import send_mail
from django.conf import settings
from .models import OrderRequest
from .forms import OrderRequestForm
from .forms import OrderResponseForm

from django.urls import reverse
import logging
logger = logging.getLogger(__name__)

def index_admin(request):
    return render(request, 'shop/index_admin.html')

def user_mode(request):
    return render(request, 'shop/index_admin/user-mode.html')

def index_shonbrunn(request):
    return render(request, 'shop/index_shonbrunn.html')

def user_mode_shonbrunn(request):
    return render(request, 'shop/index_shonbrunn/user-mode.html')

def index_hula(request):
    return render(request, 'shop/index_hula.html')

def user_mode_hula(request):
    return render(request, 'shop/index_hula/user-mode.html')

def index_api(request):
    return render(request, 'shop/index_api.html')

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
        form = OrderRequestForm(request.POST, request.FILES)  # Include request.FILES to handle file upload
        print(f"form.is_valid(): {form.is_valid()}")

        if form.is_valid():
            order = form.save()
            order_link = request.build_absolute_uri(f'/response/{order.id}/')
            send_mail(
                'New Order Submitted',
                f'An order has been submitted. View it here: {order_link}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER,
                 'vika.vinnikov@gmail.com',
                 'V0508258626@gmail.com'
],  # Replace with the actual manufacturer's email
            )
            return redirect('order_detail', pk=order.pk)
            #return redirect(reverse('order_detail', args=[order.id]))
        
            # Save the order and redirect as usual
            # order.save()
        else:
            # Print errors to the console for debugging
            print("Form errors:", form.errors.as_json())  # JSON format
            print("Form non-field errors:", form.non_field_errors())  # Non-field errors

            # Optionally, pass errors to the template to display to the user
            return render(request, 'shop/create_order.html', {'form': form})

    form = OrderRequestForm()
    return render(request, 'shop/create_order.html', {'form': form})


def order_detail(request, pk):
    logger.debug(f"Fetching order with pk={pk}")
    order = get_object_or_404(OrderRequest, pk=pk)
    logger.debug(f"Order fetched: {order.id, order.quantity, order.budget_range}")

    return render(request, 'shop/order_detail.html', {'order': order})

def order_response(request, pk):
    order = get_object_or_404(OrderRequest, pk=pk)
    logger.debug(f"Order file_price: {order.file_price}")
    
    if request.method == 'POST':
        form = OrderResponseForm(request.POST, request.FILES, instance=order)
        logger.debug(f"form.is_valid()={form.is_valid()}")

        if form.is_valid():
            form.save()

            # Prepare and send the confirmation email
            order_link = request.build_absolute_uri(f'/response/{order.id}/')
            subject = f"Order #{order.id} Updated"
            message = f"Dear {order.customer_email},\n\nYour order has been updated successfully.\n\nDetails:\n\nProducer Category: {order.get_producer_category_display()}\nBudget Range: {order.get_budget_range_display()}\nQuantity: {order.quantity}\n\nThank you for using our service! {order_link}"
            recipient_list = [order.customer_email]
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,  # Replace with the actual manufacturer's email
            )
            # Redirect back to the same page
            logger.debug(f"Order file_price: {order.file_price}")
            return redirect(reverse('order_response', args=[order.id]))
        else:
            logger.debug(f"form.errors={form.errors}")  # Log the errors to see what's causing the issue

        form = OrderResponseForm(instance=order)

    form = OrderResponseForm()
    return render(request, 'shop/order_response.html', {'form': form, 'order': order})

def send_order_email(request, pk):
    order = get_object_or_404(OrderRequest, pk=pk)
    order_link = request.build_absolute_uri(f'/order/{order.id}/')

    # Send an email to the manufacturer
    send_mail(
        'Order Information',
        f'View the order details here: {order_link}',
        settings.DEFAULT_FROM_EMAIL,
        settings.EMAIL_HOST_USER,  # Replace with actual manufacturer email
    )
