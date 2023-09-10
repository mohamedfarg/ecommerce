from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from product.models import Product
from .cart import Cart
from django.http import HttpResponse,JsonResponse

@login_required(login_url='accounts:login')
def Cart_summary(request):
    cart = Cart(request)
    total = cart.get_total_price()
    subtotal = cart.get_product_price()
    
    # return HttpResponse(cart)
    context={
        'cart_summary': cart,
        'total': total,
        'subtotal':subtotal,
        
    }
    
    return render(request, 'cart/cart.html', context)

@login_required(login_url='accounts:login')
def Cart_add(request):
    cart = Cart(request)
    print('sasa')

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=1)

        Cartqty = cart.__len__()
        response = JsonResponse({'qty': Cartqty})
        return response


@login_required(login_url='accounts:login')
def Cart_delete(request):
    
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

        Cartqty = cart.__len__()
        Carttotal = cart.get_total_price()
        response = JsonResponse({'qty': Cartqty, 'total': Carttotal})
        return response



@login_required(login_url='accounts:login')
def Cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
     
        
        cart.update(product=product_id, qty=product_qty)
        total = cart.get_total_price()
        
        Cartqty = cart.__len__()
    
        return JsonResponse({'qty': Cartqty, 'total':total})
         
 
    
    
def test(request):
    cart = Cart(request)
    return HttpResponse(cart)