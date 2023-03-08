from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_profile.models import User_Address
from user_home.models import CustomUser
from cart.cart import Cart
from admin_products.models import Product



@login_required(login_url='user_login')
def checkout(request,id,item_id):

    user = CustomUser.objects.get(id=request.user.id)

    shipping_address = User_Address.objects.filter(user = user).last()
    
    if id == 1 : # cart

        context = {
            'cart':Cart(request),
            'product':None
    }
    
    elif id == 2 : # direct checkout

        context = {
            'product': Product.objects.get(id = item_id),
            'shipping_address':User_Address.objects.filter(user = user)
        }
        # print(context['shipp'])

    # context.update(shipping_address = shipping_address )

    return render(request,'checkout/checkout.html',context)


def order_invoice(request):
    return render(request,'checkout/invoice.html')
