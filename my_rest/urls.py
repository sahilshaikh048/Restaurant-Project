from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (signup_view,login_view)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),

    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # URL for adding items to the cart
    path('cart/', views.view_cart, name='view_cart'),   # URL for viewing the cart
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('place-order/', views.place_order, name='place_order'),  # URL for placing an order
    
]