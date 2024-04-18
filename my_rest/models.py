from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Starters', 'Starters'),
        ('Main Course', 'Main Course'),
        ('Desserts', 'Desserts'),
        # Add more categories as needed
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
        
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk} - {self.user.username} - {self.created_at}"