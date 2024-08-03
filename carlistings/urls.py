from django.urls import path
from . import views

urlpatterns = [
    
    path('cars/', views.car_list, name='car_list'),
    path('add/', views.add_car, name='add_car'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
   
]
