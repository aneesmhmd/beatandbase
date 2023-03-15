from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user_profile.models import User_Address
from user_home.models import CustomUser
from admin_products.models import Product
from admin_variant.models import Product_Variant
from django.http import JsonResponse
from user_profile.forms import AddressForm
from user_profile.models import User_Address
import razorpay
from django.conf import settings
from cart.models import Cart,CartItem
from orders.models import Payment_methods



@login_required(login_url='user_login')
def checkout(request):

    global context
    if request.POST.get('action') == 'post':
        variant_id = request.POST.get('product_variant')
        variant = Product_Variant.objects.get(id = variant_id)
        product_id = request.POST.get('product_id')
        pro_qty = request.POST.get('product_quantity')
        user = CustomUser.objects.get(id=request.user.id)
        shipping_address = User_Address.objects.filter(user = user).order_by('id')
        global gst
        gst = (int(variant.price) * int(pro_qty)) * 0.05
        global total
        total = (int(variant.price) * int(pro_qty)) + gst + 100 
        form = AddressForm()
        global context
        context = {
            'shipping_address':shipping_address,
            'variant':variant,
            'quantity':pro_qty,
            'gst':gst,
            'total':total + gst,
            'form':form,
            'payment_methods': Payment_methods.objects.all()
            }

        return JsonResponse({'result':'successful'})
    else:

        client  = razorpay.Client(auth = (settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        payment = client.order.create({'amount':total*100,'currency':'INR', 'payment_capture': 1})
        
        context.update(shipping_address = User_Address.objects.filter(user = request.user.id).order_by('id'))
        context.update(payment = payment)
        return render(request,'checkout/checkout.html',context)


def cart_checkout(request):

    cartdb = Cart.objects.get(user = request.user, status = True)
    items = CartItem.objects.filter(cart = cartdb)

    shipping_address = User_Address.objects.filter(user = request.user)
    sub_total = Cart.total_item_price(cartdb)
    gst = int(sub_total) * 0.05
    total = int(sub_total) + gst + 100
    
    context  = {
        'variants':items,
        'shipping_address':shipping_address,
        'sub_total':sub_total,
        'gst':gst,
        'total':total,
        'payment_methods': Payment_methods.objects.all()
    }

    client  = razorpay.Client(auth = (settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
    payment = client.order.create({'amount':total*100,'currency':'INR', 'payment_capture': 1})
    
    context.update(shipping_address = User_Address.objects.filter(user = request.user.id).order_by('id'))
    context.update(payment = payment)

    return render(request,'checkout/cart_checkout.html',context)




 


def add_address_checkout(request):
    address = User_Address.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect(checkout)
    else:
        form = AddressForm()

