from .cart import Cart


def basket(request):
  
    cart=Cart(request)

    cart_len = cart.__len__()
  
    return {'cart_len': cart_len,'basket':cart}