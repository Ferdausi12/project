from django.db import models
from django.contrib.auth.models import User
from carlistings.models import Car

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField(default="default@example.com")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Order #{self.id} - {self.car.title} ({self.user.username})"
    
    
    


    
    

