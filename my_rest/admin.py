from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    list_filter = ('category',)

admin.site.register(MenuItem, MenuItemAdmin)