from django.shortcuts import redirect
from django.contrib.auth import logout


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('backend:dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def is_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_admin:
            return view_func(request, *args, **kwargs)
        else:
            logout(request)
            return redirect('backend:login')
    return wrapper_func