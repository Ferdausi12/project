from django.urls import path
from . import views

urlpatterns = [
    path('place_order/<int:car_id>/', views.place_order, name='place_order'),
    path('process_order/<int:car_id>/', views.process_order, name='process_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('orders/', views.order_list, name='order_list'),
    path('my-orders/', views.user_orders, name='user_orders'),
]
