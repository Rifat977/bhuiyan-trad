from django.contrib import admin
from .models import *

# Register your models here.
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'phone', 'created_date')
    search_fields = ('name', 'number')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'Category')
    search_fields = ('name', 'slug')

    def Category(self, obj):
        return obj.category.name

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(User,)
admin.site.register(Admin, AdminAdmin)