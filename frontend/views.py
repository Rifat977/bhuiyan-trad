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

def Subcategory(request, cat_id):
    settings = Settings.objects.first()
    subcategory = Subcategory.objects.filter()
    context = {
        'settings' : settings,
        'category' : category,
        'product' : product
    }
    return render(request, 'subcategory.html', context)

