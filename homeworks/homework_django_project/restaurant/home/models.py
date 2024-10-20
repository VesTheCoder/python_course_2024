from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='dishes')
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

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True).order_by('sort')
        for dish in dishes:
            yield dish

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
    twitter = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class RestaurantContact(models.Model):
    item_title = models.CharField(max_length=80, null=False, blank=False, default='lol')
    item_description = RichTextField(default='lol')
    item_icon = models.CharField(max_length=250, default='lol')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.item_title
    
class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?3?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=25, validators=[phone_regex])
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField(null=False, blank=False)
    message = models.TextField(null=True, blank=True)
    is_processed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class FooterItem(models.Model):
    item_title = models.CharField(max_length=80, null=False, blank=False, default='lol')
    item_description = RichTextField(default='lol', null=True, blank=True)
    item_icon = models.CharField(max_length=250, default='lol', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_title