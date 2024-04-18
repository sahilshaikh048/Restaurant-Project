from django.shortcuts import render
from .models import MenuItem

def index(request):
    return render(request, 'my_rest/index.html')

def menu(request):
    # Fetch all menu items from the database
    menu_items = MenuItem.objects.all()
    # Pass the menu items to the template
    return render(request, 'my_rest/menu.html', {'menu_items': menu_items})

def about(request):
    return render(request, 'my_rest/about.html')

def reservation(request):
    return render(request, 'my_rest/reservation.html')

def contact(request):
    return render(request, 'my_rest/contact.html')
