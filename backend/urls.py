from django.urls import path
from . import views

app_name = "backend"

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),

    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
]
