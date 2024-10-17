from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/', null=False, blank=False)
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to='events/', null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Worker(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    position = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='workers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class RestaurantContact(models.Model):
    address = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    opening_hours = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return f'Restaurant at {self.address}'