from django.contrib import admin
from carlistings.models import Car
from orders.models import Order

class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'condition', 'created_at')
    list_filter = ('condition', 'created_at')
    search_fields = ('title', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('car__title', 'user__username')

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
