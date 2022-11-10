from django.shortcuts import render
from backend.models import *

# Create your views here.
def Home(request):
    settings = Settings.objects.first()
    category = Category.objects.all().order_by('-id')
    product = Product.objects.all()
    context = {
        'settings' : settings,
        'category' : category,
        'product' : product
    }
    return render(request, 'home.html', context)

def SubcategoryView(request, cat_id):
    settings = Settings.objects.first()
    subcategory = Subcategory.objects.filter(category_id=cat_id)
    single_category = Category.objects.get(id=cat_id)
    context = {
        'settings' : settings,
        'subcategory' : subcategory,
        'single_category' : single_category
    }
    return render(request, 'subcategory.html', context)

def SubcategoryProductView(request, sub_id):
    settings = Settings.objects.first()
    single_subcategory = Subcategory.objects.get(category_id=sub_id)
    product = Product.objects.filter(subcategory=sub_id)
    context = {
        'settings' : settings,
        'single_subcategory' : single_subcategory,
        'product' : product
    }
    return render(request, 'subcategory-product.html', context)


def ProductView(request, pro_id):
    settings = Settings.objects.first()
    product = Product.objects.get(id=pro_id)
    galleryImage = GalleryImage.objects.filter(product_id=pro_id)
    context = {
        'settings' : settings,
        'product' : product,
        'galleryImage': galleryImage
    }
    return render(request, 'single-product.html', context)
