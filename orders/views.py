from django.shortcuts import render,redirect
from user_home.models import CustomUser
from user_profile.models import User_Address
from admin_variant.models import Product_Variant
from django.http import JsonResponse
from .models import Order,Order_item,Payment_methods
import json
from cart.models import Cart,CartItem

def place_order(request):
    
    if request.POST.get('action') == 'post' and request.POST.get('from') == 'cart':

        # getting user details
        user = request.user
        user = CustomUser.objects.get(id = user.id)

        # getting cart details    
        cartdb = Cart.objects.get(user=user, status=True)
        cart_items = CartItem.objects.filter(cart=cartdb)
        
        # getting values form requests
        total = float(request.POST.get('total') )
        gst = float(request.POST.get('gst') )
        address_id = request.POST.get('shipping_address')
        payment_method = request.POST.get('payment_method')

        # getting needed instances from id's
        shipping_address = User_Address.objects.get(id = address_id)
        payment_method = Payment_methods.objects.get(id = payment_method)

        # placing order
        current_order = Order.objects.create(customer=user, address=shipping_address,gst=gst, total=total, payment_method=payment_method)
        for variant in cart_items:
            Order_item.objects.create(order=current_order,variant=variant.variant,quantity=variant.qty)
        
        # making order placed status FALSE
        cartdb.status = False
        cartdb.delete()

        return render(request,'orders/invoice.html')
        
    elif request.POST.get('action') == 'post' and request.POST.get('from') == 'direct':

        # getting user details
        user = request.user
        user = CustomUser.objects.get(id = user.id)

        # getting values form requests
        total = float(request.POST.get('total') )
        variant = int(request.POST.get('variant') )
        quantity = int(request.POST.get('quantity') )
        gst = float(request.POST.get('gst') )
        address_id = request.POST.get('shipping_address')
        payment_method = request.POST.get('payment_method')

        # getting needed instances from id's
        shipping_address = User_Address.objects.get(id = address_id)
        payment_method = Payment_methods.objects.get(id = payment_method)
        variant = Product_Variant.objects.get(id = variant)

        # placing order
        current_order = Order.objects.create(customer=user, address=shipping_address,gst=gst, total=total, payment_method=payment_method)
        Order_item.objects.create(order=current_order,variant=variant,quantity=quantity)

        return JsonResponse({'order_id':current_order.id})
        



def order_invoice(request):

    # getting order item details for showing in invoice
   order_id = int(request.GET.get('id'))
   order = Order.objects.get(id = order_id)
   order_item = Order_item.objects.filter(order=order)

    # calculatin toal amout of order 
   def get_sub_total():
       sub_total = 0
       for item in order_item:
           sub_total += int(item.variant.price) * int(item.quantity)

       return sub_total
   
   context = {
      'order':order,
      'items':order_item,
      'sub_total':get_sub_total()
   }

   return render(request,'orders/invoice.html',context)



def user_orders(request):

    current_order = Order.objects.filter(customer=request.user)

    order_items = Order_item.objects.filter(order__customer=request.user).order_by('-id')

        
    context = {
        'orders': current_order,
        'order_items': order_items,
    }
    return render(request,'orders/user_orders.html',context)