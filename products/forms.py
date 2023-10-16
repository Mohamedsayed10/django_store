from django import forms
from .models import Product,Category

class Productform(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())




