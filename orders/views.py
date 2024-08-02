from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order
from .forms import OrderForm
from carlistings.models import Car

# Create your views here.



def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})




def place_order(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = car.price * quantity
            order = form.save(commit=False)
            order.user = request.user
            order.car = car
            order.total_price = total_price
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form, 'car': car})



@login_required
def process_order(request, car_id):
    car = Car.objects.get(pk=car_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            buyer_name = form.cleaned_data['buyer_name']
            buyer_email = form.cleaned_data['buyer_email']
            quantity = form.cleaned_data['quantity']
            
           
            car_price = car.price
            total_price = quantity * car_price  
            
            
            order = Order(
                car=car,
                buyer_name=buyer_name,
                buyer_email=buyer_email,
                quantity=quantity,
                total_price=total_price,
                user=request.user  
            )
            order.save()
            return redirect('order_success')  
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'car_id': car_id,
    }
    return render(request, 'orders/place_order.html', context)
def order_success(request):
    return render(request, 'order_success.html')


@staff_member_required
def admin_dashboard(request):
    
    orders = Car.objects.all()
    return render(request, 'admin_dashboard.html', {'orders': orders})

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {'orders': orders})


