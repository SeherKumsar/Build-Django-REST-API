from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: # Bir model formunun nasıl davranacağını ve hangi modelle ilişkili olacağını belirlemek için kullanılır
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]