from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ('user',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'