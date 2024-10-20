from .models import FooterItem

def footer_items(request):
    context = {}
    footer_items = FooterItem.objects.all()

    for item in footer_items:
        if item.item_title == 'Address':
            context['address'] = item
        if item.item_title == 'Reservations':
            context['reservations'] = item
        if item.item_title == 'Opening Hours':
            context['opening_hours'] = item




    return {
        'footer_items': context,
    }