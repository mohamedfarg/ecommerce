from django.shortcuts import render,get_object_or_404,redirect
from cart.cart import Cart
from datetime import timezone,datetime
import uuid
from django.contrib.auth.models import User
from .models import Order, OrderItem
from django.http.response import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
@login_required(login_url='accounts:login')
def add(request):
    basket = Cart(request)
    if request.method == 'POST':
        user = request.user
        baskettotal = basket.get_total_price()
        
        # Generate a unique order key
        order_key = str(uuid.uuid4())
        
        # Check if order exists
        order = Order.objects.create(
            customer_id=user,
            full_name=user.first_name or "guest",
            address1='add1',
            address2='add2',
            phone="phone",
            total_paid=baskettotal,
            order_key=order_key
        )
        for item in basket:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['qty']
            )
            
        subject = "Order confirmation"  # Removed the comma at the end of this line
        message = f"Your order has been created with id : {order.id}."  # Removed the comma at the end of this line
        from_email = 'farag92mohamed@gmail.com'
        to_email = 'medo.farg50@gmail.com'  # Added the missing 'to_email' variable

        send_mail(subject, message, from_email, [to_email])  # Wrap 'to_email' in a list

                
       
        
        return redirect("products:home")
        # return JsonResponse({'status':"success"})

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    return orders

# def create_coupon(request, product_id, discount):
#     coupon = Coupon.objects.create(
#         code=uuid.uuid4().hex,
#         discount=discount,
#         start_date=timezone.now(),
#         end_date=timezone.now() + datetime.timedelta(days=30),
#         active=True,
#         product_id=product_id
#     )
#     return redirect('coupons')