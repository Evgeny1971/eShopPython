# shop/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', default='default_images/default_image.jpg')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer_address = models.CharField(max_length=255)
    order_details = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    uploaded_file = models.FileField(upload_to='orders/', null=True, blank=True)  # New field for file upload

    def __str__(self):
        return f"Order {self.id} - {self.customer_address}"
