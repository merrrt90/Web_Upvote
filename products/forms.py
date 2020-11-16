from django import forms
from .models import Product, ProductCategory, Images


class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'title', 'placeholder': 'Please Enter Title'}),
        label="Title")
    website = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'website', 'placeholder': 'Paste Your Website Link'}),
        label="Website")
    youtube = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'youtube', 'placeholder': 'Paste Your Youtube Video Url'}),
        label="Youtube Link")
    slug = forms.SlugField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'slug', 'placeholder': 'Enter Your Slug Without empty space'}),
        label="Slug")
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'description', 'placeholder': 'Enter Your Product Short Description'}),
        label="Description")
    icon = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'rounded_list'})),
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea', 'type': 'text', 'name': 'body', 'placeholder': 'Enter Your Product Description'}),
        label="Body")

    '''added attributes so as to customise for styling, like bootstrap'''
    class Meta:
        model = Product
        fields = ['title', 'website', 'youtube', 'slug',
                  'description', 'icon', 'body', 'category']
