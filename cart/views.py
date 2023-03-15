from django.shortcuts import render,redirect
from admin_products.models import Product
from django.shortcuts import get_object_or_404
from .cart import Cart as Cart_session
from admin_variant.models import Product_Variant
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart,CartItem
from user_home.models import CustomUser



@login_required(login_url='user_login')
def cart_summary(request):

    cart,_ = Cart.objects.get_or_create(user = request.user, status = True)
    cart_items = CartItem.objects.filter(cart = cart)

    def get_total():
        global sub_total
        sub_total = 0
        for item in cart_items:
            sub_total +=item.variant.price * item.qty
        global gst
        gst = sub_total *0.05
        global grand_total
        grand_total = sub_total + gst + 100
        return sub_total
    






    # cart = Cart_session(request)
    variants = Product_Variant.objects.all()

    return render(request,'cart/cart.html',{'cart':cart_items,'variants':variants,'sub_total':get_total(),'gst':gst,'grand_total':grand_total })


@login_required(login_url='user_login')
def cart_add(request):

    if request.POST.get('action') == 'post':

        # getting user 
        user = request.user
        user = CustomUser.objects.get(id = user.id)

        # getting cart item 
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        variant = request.POST.get('product_variant')

        # getting needed cart item details from models
        product = get_object_or_404(Product, id=product_id)
        variant_instance = Product_Variant.objects.get(id = variant)
        price = variant_instance.price
        color = variant_instance.color

        # saving cart to database
        cartdb, _ = Cart.objects.get_or_create(user = user, status = True) 
        item = CartItem.objects.create( cart = cartdb, variant=variant_instance, qty=product_quantity )
        item.save

        # save to session
        cart = Cart_session(request)
        cart.add(variant=variant_instance, product=product, color=color, price=price, product_qty=product_quantity)
        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': product_quantity,'cart_qty':cart_quantity})
        return response
    
def add_quantity(request):

    if request.POST.get('action') == 'post':

        product_id = request.POST.get('product_id')

        response = JsonResponse({'result':f'its working,{product_id}'})
        return response


def cart_delete(request):

    cart = Cart_session(request)

    if request.POST.get('action') == 'post':

        variant_id = int(request.POST.get('variant_id'))
        variant_instance = Product_Variant.objects.get(id = variant_id)

        cart.delete(variant=variant_id)

        # delete cart from db
        cartdb = Cart.objects.get(user = request.user, status = True)
        item = CartItem.objects.get(cart = cartdb, variant=variant_instance )
        item.delete()


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})

        return response




def cart_update(request):

    cart = Cart_session(request)

    if request.POST.get('action') == 'post':

        variant_id = int(request.POST.get('variant_id'))
        product_quantity = int(request.POST.get('product_quantity'))
    

        cart.update(variant=variant_id, qty=product_quantity)

        variant_instance = Product_Variant.objects.get(id = variant_id)
        cartdb = Cart.objects.get(user = request.user, status = True)
        item = CartItem.objects.get(cart = cartdb, variant=variant_instance )
        item.qty = product_quantity
        item.save()

        cart_quantity = cart.__len__()

        cart_total = cart.get_total()

        cart_gst = cart.get_gst()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total, 'gst':cart_gst})

        return response


