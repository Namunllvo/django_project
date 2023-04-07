# # erps/forms.py
from django import forms
from .models import Product


# form - 상품등록
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']

# Form - 예제
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

# form - 입고
class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['goods', 'amount', 'price_']

# # form - 출고
class OutboundForm(forms.ModelForm):
    pass