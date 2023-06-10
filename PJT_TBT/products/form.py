from django import forms
from .models import Product, ProductImage

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "pay", "Description1", "Description2", "delivery","sale",]
        labels = {
            "name": "상품명",
            "category": "상품분류",
            "pay": "상품가격",
            "sale": "할인율", 
            "Description1": "상품설명(text)",
            "Description2": "상품설명(image)",
            "delivery": "배송비",

        }

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='상품이미지',
        widget=forms.ClearableFileInput(attrs={'multiple':True}),
    )
    class Meta:
        model = ProductImage
        fields = ('image', )