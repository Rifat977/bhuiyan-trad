from django.shortcuts import render
from backend.models import *
from backend.forms import ContactForm
from django.contrib import messages
from django.db.models import Q 

# Create your views here.
def Home(request):
    settings = Settings.objects.first()
    category = Category.objects.all().order_by('-id')
    product = Product.objects.all()[:4]
    sponsor = Sponsor.objects.all()
    context = {
        'settings' : settings,
        'category' : category,
        'product' : product,
        'sponsor' : sponsor
    }
    return render(request, 'home.html', context)

def SubcategoryView(request, cat_id):
    settings = Settings.objects.first()
    subcategory = Subcategory.objects.filter(category_id=cat_id)
    # single_category = Category.objects.first(id=cat_id)
    context = {
        'settings' : settings,
        'subcategory' : subcategory,
        # 'single_category' : single_category
    }
    return render(request, 'subcategory.html', context)

def SubcategoryProductView(request, sub_id, subcategory_name):
    settings = Settings.objects.first()
    product = Product.objects.filter(subcategory=sub_id)
    context = {
        'settings' : settings,
        'single_subcategory' : subcategory_name,
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

def ContactView(request):
    settings = Settings.objects.first()
    context = {
        'settings' : settings,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', context)
        else:
            print(form.errors.as_data())
    return render(request, 'contact.html', context)


def AllProductView(request):
    pg = 10
    settings = Settings.objects.first()
    product = Product.objects.all().order_by('-id')[:pg]
    subcategory = Subcategory.objects.all().order_by('name')
    if 'page' in request.GET:
        page = int(request.GET['page'])
        pg += page
        product = Product.objects.all().order_by('-id')[:pg]
    if 'search' in request.GET:
        search = request.GET['search']
        product = Product.objects.filter(Q(name__icontains = search))
    context = {
        'settings' : settings,
        'product' : product,
        'subcategory': subcategory,
        'pg' : pg
    }
    return render(request, 'products.html', context)

def AboutView(request):
    settings = Settings.objects.first()
    about = About.objects.all()
    context = {
        'settings' : settings,
        'about' : about
    }
    return render(request, 'about.html', context)
