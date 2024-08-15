# shop/models.py
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', default='default_images/default_image.jpg')

    def __str__(self):
        return self.name
    
class OrderRequest(models.Model):
    PRODUCER_CATEGORIES = [
        (1, 'Welding'),
        (2, 'Metalworking'),
        (3, 'Sewing'),
    ]

    BUDGET_RANGES = [
        (1, 'Under $1,000'),
        (2, '$1,000 - $5,000'),
    ]

    PAYMENT_METHODS = [
        (1, 'Prepayment'),
        (2, 'Partial Prepayment'),
        (3, 'Payment upon Completion'),
    ]

    MATERIAL_SOURCES = [
        (1, 'Supplier Provided'),
        (2, 'Client Provided'),
        (3, 'Other'),
    ]

    DELIVERY_OPTIONS = [
        (1, 'Standard Delivery'),
        (2, 'Express Delivery'),
        (3, 'Pickup'),
    ]

    customer_email = models.EmailField()
    producer_category = models.IntegerField(choices=PRODUCER_CATEGORIES,default=1)
    budget_range = models.IntegerField(choices=BUDGET_RANGES,default=1)
    quantity = models.PositiveIntegerField(default=1)
    payment_method = models.IntegerField(choices=PAYMENT_METHODS,default=1)
    material_source = models.IntegerField(choices=MATERIAL_SOURCES,default=1)
    delivery_option = models.IntegerField(choices=DELIVERY_OPTIONS,default=1)
    delivery_deadline = models.DateTimeField(default=timezone.now)
    agree_to_penalties = models.BooleanField(default=False)
    agree_to_bonuses = models.BooleanField(default=False)
    agree_to_arbitrator = models.BooleanField(default=False)
    additional_information = models.TextField(blank=True)
    file_attachments = models.FileField(upload_to='order_files/', null=True, blank=True)
    file_count = models.PositiveIntegerField(default=1)  # New field for file count
    shipping_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"OrderRequest {self.id} - {self.customer_email}"
