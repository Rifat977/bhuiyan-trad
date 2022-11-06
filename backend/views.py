from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# Create your views here.
@login_required
def Dashboard(request):
    return render(request, 'admin/dashboard.html')

@unauthenticated_user
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_admin:
                messages.info(request, "this is admin")
            elif user.is_superuser:
                messages.info(request, "this is superuser")
            # login(request, user)
            # return redirect('backend:dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')

@login_required
def Logout(request):
    logout(request)
    return redirect('backend:login')