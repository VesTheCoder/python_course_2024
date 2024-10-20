from django.shortcuts import render
from .models import Category, Event, GalleryPhoto, RestaurantContact, Worker
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservation_success = False  # Флаг успешной резервации

    if request.method == 'POST':
        book_table_form = ReservationForm(request.POST)
        if book_table_form.is_valid():
            book_table_form.save()
            reservation_success = True  # Устанавливаем флаг в True после успешной отправки формы

    else:
        book_table_form = ReservationForm()

    categories = Category.objects.filter(is_visible=True).order_by('sort')
    gallery = GalleryPhoto.objects.filter(is_visible=True).order_by('sort')
    events = Event.objects.filter(is_visible=True).order_by('sort')
    worker = Worker.objects.filter(is_visible=True).order_by('sort')
    contacts = RestaurantContact.objects.filter(is_visible=True)
    book_table_form = ReservationForm()

    context = {
        'categories': categories,
        'gallery': gallery,
        'events': events,
        'book_table_form': book_table_form,
        'worker': worker,
        'contacts': contacts,
        'reservation_success': reservation_success
    }

    return render(request, 'index.html', context)
