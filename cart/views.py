from django.shortcuts import render,redirect
from admin_products.models import Product
from django.shortcuts import get_object_or_404
from .cart import Cart
from admin_variant.models import Product_Variant
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url='user_login')
def cart_summary(request):

    cart = Cart(request)
    variants = Product_Variant.objects.all()

    return render(request,'cart/cart.html',{'cart':cart,'variants':variants})




def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        print(request.POST.get('product_id'))
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        variant = request.POST.get('product_variant')
        product = get_object_or_404(Product, id=product_id)
        variant_instance = Product_Variant.objects.get(id = variant)
        price = variant_instance.price
        color = variant_instance.color
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

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        variant_id = int(request.POST.get('variant_id'))

        cart.delete(variant=variant_id)


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})

        return response




def cart_update(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        variant_id = int(request.POST.get('variant_id'))
        print(variant_id)
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(variant=variant_id, qty=product_quantity)


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()

        cart_gst = cart.get_gst()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total, 'gst':cart_gst})

        return response


