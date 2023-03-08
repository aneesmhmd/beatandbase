from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Wishlist
from admin_products.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='user_login')
def wishlist(request):
    usr = request.user.id
    try:
        product = Wishlist.objects.filter(user = usr)
    except:
        product = ''  
    return render(request,'wishlist/wishlist.html',{'products':product})

@login_required
def add_wishlist(request, product_id):
    user = request.user
    try:
        wishlist = Wishlist.objects.get(user=user, product=product_id)
    except Wishlist.DoesNotExist:
        product = Product.objects.get(id=product_id)
        wishlist = Wishlist(user=user, product=product)
        wishlist.save()
    return redirect('product_detail', product_id)

def delete_wishlist(request,product_id):
    usr = request.user.id
    print(product_id)
    product = Wishlist.objects.get(user = usr ,product = product_id)
    product.delete()
    # messages.info(request,'something went wrong!') 
    return redirect(wishlist)