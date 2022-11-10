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

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('image',)
    
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'