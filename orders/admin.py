from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user', 'buyer_name', 'status', 'quantity', 'total_price', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('car__title', 'user__username', 'buyer_name', 'buyer_email')
    readonly_fields = ('ordered_at',)
    list_editable = ('status',)
    
# admin.site.register(Order, OrderAdmin)
