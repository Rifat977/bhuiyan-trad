from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="home"),
    path('subcategory/<int:cat_id>', views.Subcategory, name="subcategory"),
]
