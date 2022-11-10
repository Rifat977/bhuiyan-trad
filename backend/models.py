from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from datetime import date
import random

rand = random.randint(10000,99999)
today = date.today()
rand = str(rand)+str(today)+str(rand)
 
# Create your models here.
def category_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (rand, ext)
    return os.path.join('category', filename)

def user_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (rand, ext)
    return os.path.join('user', filename)

def product_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (rand, ext)
    return os.path.join('product', filename)

def settings_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (rand, ext)
    return os.path.join('settings', filename)

class User(AbstractUser):
    @property
    def is_admin(self):
        if hasattr(self, 'admin'):
            return True
        return False

class Settings(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    site_logo = models.ImageField(upload_to=settings_path)
    hero_image = models.ImageField(upload_to=settings_path)
    who_we = models.TextField()
    who_we_image = models.ImageField(upload_to=settings_path)
    future_focused = models.TextField()
    future_forused_img = models.ImageField(upload_to=settings_path)
    about_us = models.TextField()
    about_us_img = models.ImageField(upload_to=settings_path)   
 

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=220, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    image = models.ImageField(upload_to=user_path, blank=True);
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_admin(sender, instance, created, **kwargs):
    if created:
        Admin.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_admin(sender, instance, **kwargs):
    instance.admin.save()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=category_path, null=False, blank=False, default="default.jpg")

    @property
    def slug(self):
        name = self.name
        return name.replace(' ', '-').lower()
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=category_path, null=False, blank=False, default="default.jpg")

    @property
    def slug(self):
        name = self.name
        return name.replace(' ', '-').lower()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(blank=True, default=0)
    currency = models.CharField(max_length=25, blank=True, default="BDT")
    stock = models.IntegerField(blank=True, default=0)
    shortdesc = models.TextField(null=True, blank=True)
    productdesc = models.TextField(null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    featureimage = models.ImageField(upload_to=product_path, null=False, blank=False)

    @property
    def slug(self):
        name = self.name
        return name.replace(' ', '-').lower()

class GalleryImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_path, default=None)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    product_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()

class About(models.Model):
    image = models.ImageField(upload_to=settings_path, blank=True)
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)


