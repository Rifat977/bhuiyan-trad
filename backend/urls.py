from django.urls import path
from . import views

app_name = "backend"

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),

    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),

    path('profile/', views.Profile, name="profile"),

    path('add-category/', views.AddCategory, name="add-category"),
    path('edit-category/<int:pk>/', views.EditCategory, name="edit-category"),
    path('delete-category/<int:pk>', views.DeleteCategory, name="delete-category"),
    path('add-subcategory/', views.AddSubcategory, name="add-subcategory"),
     path('edit-subcategory/<int:pk>', views.EditSubcategory, name="edit-subcategory"),
    path('delete-subcategory/<int:pk>', views.DeleteSubcategory, name="delete-subcategory"),

    path('add-product/', views.AddProduct, name="add-product"),
    path('products/', views.ProductsView, name="products"),
    path('categories/', views.CategoryView, name="categories"),
]
