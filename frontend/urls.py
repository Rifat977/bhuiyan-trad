from django.urls import path
from . import views

app_name = "frontend"

urlpatterns = [
    path('', views.Home, name="home"),
    path('subcategory/<int:cat_id>', views.SubcategoryView, name="subcategory"),
    path('subcategory/product/<int:sub_id>', views.SubcategoryProductView, name="subcategory-product"),
]
