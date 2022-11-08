from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
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

class User(AbstractUser):
    @property
    def is_admin(self):
        if hasattr(self, 'admin'):
            return True
        return False

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to=user_path);
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

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