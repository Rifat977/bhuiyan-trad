from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, is_admin
from django.conf import settings
from .forms import *

# Create your views here.
@login_required
def Dashboard(request):
    category = Category.objects.all().count()
    subcategory = Subcategory.objects.all().count()
    product = Product.objects.all().count()
    context = {
        'category' : category,
        'subcategory': subcategory,
        'product' : product
    }
    return render(request, 'admin/dashboard.html', context)

@unauthenticated_user
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_admin:
                login(request, user)
                messages.success(request, "Welcome, "+request.user.admin.name+"! You are Logged in!")
                return redirect('backend:dashboard')
            elif user.is_superuser:
                messages.error(request, 'Username or password is incorrect')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')

@login_required
def Logout(request):
    logout(request)
    return redirect('backend:login')

@login_required
def AddCategory(request):
    if request.method=="POST":
        form = CategoryForm(request.POST, request.FILES)
        errors = []
        if form.is_valid():
            form.save();
            messages.success(request, "Category created successfully!")
        else:
            if(request.POST['name']==''):
                errors.append("The name field is required!")
            if Category.objects.exclude(name=request.POST['name']).exists():
                errors.append("Category already exists!")
            return render(request, 'admin/add_category.html', {'errors':errors})
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'admin/add_category.html', context)

@login_required
def EditCategory(request, pk):
    errors = []
    if request.method=="POST":
        name = request.POST['name']
        entry = Category.objects.get(id=pk)
        old_img = entry.image.path
        form = CategoryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            if request.FILES:
                if(os.path.exists(old_img)):
                    os.remove(old_img)
            form.save();
            messages.success(request, "Category updated successfully!")
            return redirect('backend:categories')
        else:
            if name=="":
                errors.append("The name field is required!")
            else:
                try:
                    Category.objects.filter(id=pk).update(name=name)
                    return redirect('backend:categories')
                except Exception:
                    errors.append("Already updated")
    cat = Category.objects.get(id=pk)
    context = {
        'category':cat,
        'errors': errors
    }
    return render(request, 'admin/edit/category.html', context)

@login_required
def DeleteCategory(request, pk):
    cat = Category.objects.get(id=pk)
    old_img = cat.image.path
    if(os.path.exists(old_img)):
        os.remove(old_img)
    cat.delete()
    return redirect('backend:categories')

@login_required
def AddSubcategory(request):
    if request.method=="POST":
        sub_name = request.POST["name"]
        cat_name = request.POST["category"]
        form = SubcategoryForm(request.POST, request.FILES)
        errors = []
        if form.is_valid():
            form.save();
            messages.success(request, "Subcategory created successfully!")
        else:
            if(sub_name==''):
                errors.append("The subcategory field is required!")
            if(cat_name==''):
                errors.append("The category field is required!")
            if Subcategory.objects.exclude(name=sub_name).exists():
                errors.append("Subcategory already exists!")       
            return render(request, 'admin/add_category.html', {'errors':errors})
        return redirect('backend:add-category')

@login_required
def EditSubcategory(request, pk):
    errors = []
    if request.method=="POST":
        name = request.POST['name']
        category = request.POST['category']
        print(name, category)
        entry = Subcategory.objects.get(id=pk)
        old_img = entry.image.path
        form = SubcategoryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            if request.FILES:
                if(os.path.exists(old_img)):
                    os.remove(old_img)
            form.save();
            messages.success(request, "Subcategory updated successfully!")
            return redirect('backend:categories')
        else:
            if name=="":
                errors.append("The name field is required!")
            else:
                try:
                    entry.name = name
                    entry.category = category
                    entry.save()
                    return redirect('backend:categories')
                except Exception:
                    errors.append("Already updated")
    subcategory = Subcategory.objects.get(id=pk)
    category = Category.objects.all()
    context = {
        'subcategory':subcategory,
        'errors': errors,
        'category': category,
    }
    return render(request, 'admin/edit/subcategory.html', context)

@login_required
def DeleteSubcategory(request, pk):
    subcat = Subcategory.objects.get(id=pk)
    old_img = subcat.image.path
    if(os.path.exists(old_img)):
        os.remove(old_img)
    subcat.delete()
    return redirect('backend:categories')

@login_required
def AddProduct(request):
    error = []
    if request.method == "POST":
        name = request.POST['name']
        # galleryImage = request.FILES.getlist('galleryimage')
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            for validation_error in form.errors.as_data():
                error.append(validation_error + " field is required")
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        'category': category,
        'subcategory': subcategory,
        'errors' : error
    }
    return render(request, 'admin/add_product.html', context)

@login_required
def ProductsView(request):
    product = Product.objects.all().order_by('-id')
    context = {
        'product' : product
    }
    return render(request, 'admin/products.html', context)

@login_required
def EditProduct(request, pk):
    entry = Product.objects.get(id=pk)
    old_img = entry.featureimage.path
    error = []
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            if request.FILES:
                if(os.path.exists(old_img)):
                    os.remove(old_img)
            form.save()
            messages.success(request, "Product update successfully!")
            return redirect('backend:products')
        else:
            for validation_error in form.errors.as_data():
                error.append(validation_error + " field is required")
    product = Product.objects.get(id=pk)
    subcategory = Subcategory.objects.all()
    context = {
        'product' : product,
        'subcategory': subcategory,
        'errors' : error
    }
    return render(request, 'admin/edit/product.html', context)

@login_required
def CategoryView(request):
    categories = Category.objects.all().order_by('-id')
    subcategoires = Subcategory.objects.all().order_by('-id')
    context = {'categories':categories, 'subcategoires': subcategoires}
    return render(request, 'admin/categories.html', context)

@login_required
def DeleteProduct(request, pk):
    entry = Product.objects.get(id=pk)
    old_img = entry.featureimage.path
    if(os.path.exists(old_img)):
        os.remove(old_img)
    entry.delete()
    return redirect('backend:products')

@login_required
@is_admin
def Profile(request):
    user = Admin.objects.get(user=request.user)
    old_img = user.image.path
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            if request.FILES:
                    if(os.path.exists(old_img)):
                        os.remove(old_img)
            form.save();
            messages.success(request, "Profile updated successfully!")
            return redirect('backend:profile')
        else:
            print(form.errors.as_data())
    return render(request, 'profile.html')