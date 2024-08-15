
# shop/forms.py
from django import forms
from .models import Product
from .models import OrderRequest


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

class OrderRequestForm(forms.ModelForm):
    producer_category = forms.ChoiceField(
        choices=OrderRequest.PRODUCER_CATEGORIES,
        widget=forms.RadioSelect,
        required=False
    )

    class Meta:
        model = OrderRequest
        fields = [
            'producer_category',
            'budget_range',
            'quantity',
            'customer_email',
            'payment_method',
            'material_source',
            'delivery_option',
            'delivery_deadline',
            'agree_to_penalties',
            'agree_to_bonuses',
            'agree_to_arbitrator',
            'file_attachments',
            'file_count',  # New field for file count
            'additional_information',
            'shipping_address',
            'city',
            'state',
        ]
    #quantity = forms.IntegerField(required=False)
    #customer_email = forms.EmailField(required=False)
    #state = forms.CharField(required=False)


