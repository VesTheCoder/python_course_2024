from django.contrib import admin

# Register your models here.

from .models import Category, Dish, Event, GalleryPhoto, RestaurantContact, Worker

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'sort', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    list_filter = ['is_visible', 'created_at', 'updated_at']
    list_editable = ['is_visible', 'sort']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'is_visible', 'sort', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['is_visible', 'created_at', 'updated_at']
    list_editable = ['is_visible', 'sort']
    date_hierarchy = 'created_at'

admin.site.register(Event)
admin.site.register(GalleryPhoto)
admin.site.register(RestaurantContact)
admin.site.register(Worker)