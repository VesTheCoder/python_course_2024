from django.contrib import admin
from .models import Category, Dish, Event, GalleryPhoto, RestaurantContact, Worker, Reservation, FooterItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'sort', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    list_filter = ['is_visible', 'created_at', 'updated_at']
    list_editable = ['is_visible', 'sort']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ['sort', 'name']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'is_visible', 'sort', 'created_at', 'updated_at']
    search_fields = ['name', 'description', 'category__name']
    list_filter = ['is_visible', 'category', 'created_at', 'updated_at']
    list_editable = ['is_visible', 'sort']
    date_hierarchy = 'created_at'
    ordering = ['sort', 'name']
    autocomplete_fields = ['category']

class DishInline(admin.TabularInline):
    model = Dish
    extra = 1
    fields = ['name', 'price', 'is_visible', 'sort']
    show_change_link = True

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'time', 'price', 'is_visible', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['is_visible', 'date', 'created_at', 'updated_at']
    date_hierarchy = 'date'
    ordering = ['date', 'title']
    list_editable = ['is_visible']

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_visible', 'sort', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['is_visible', 'created_at', 'updated_at']
    list_editable = ['is_visible', 'sort']
    ordering = ['sort', 'title']

@admin.register(RestaurantContact)
class RestaurantContactAdmin(admin.ModelAdmin):
    list_display = ['item_title', 'is_visible', 'created_at', 'updated_at']
    search_fields = ['item_title']
    list_filter = ['is_visible', 'created_at', 'updated_at']
    list_editable = ['is_visible']
    ordering = ['item_title']

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'sort', 'created_at', 'updated_at']
    search_fields = ['name', 'position', 'description']
    list_filter = ['is_visible', 'created_at', 'updated_at']
    list_editable = ['is_visible', 'sort']
    ordering = ['sort', 'name']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date', 'time', 'number_of_guests', 'is_processed', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['is_processed', 'date', 'created_at', 'updated_at']
    list_editable = ['is_processed']
    date_hierarchy = 'date'
    ordering = ['-date', '-time']

@admin.register(FooterItem)
class FooterItemAdmin(admin.ModelAdmin):
    list_display = ['item_title', 'created_at', 'updated_at']
    search_fields = ['item_title']
    list_filter = ['created_at', 'updated_at']
    ordering = ['item_title']