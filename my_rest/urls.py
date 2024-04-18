from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
]
