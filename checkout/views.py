from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user_profile.models import User_Address
from user_home.models import CustomUser
from cart.cart import Cart
from admin_products.models import Product
from admin_variant.models import Product_Variant
from django.http import JsonResponse
from user_profile.forms import AddressForm
from user_profile.models import User_Address



@login_required(login_url='user_login')
def checkout(request):

    global context
    if request.POST.get('action') == 'post':
        variant_id = request.POST.get('product_variant')
        variant = Product_Variant.objects.get(id = variant_id)
        product_id = request.POST.get('product_id')
        pro_qty = request.POST.get('product_quantity')
        user = CustomUser.objects.get(id=request.user.id)
        shipping_address = User_Address.objects.filter(user = user).order_by('-id')
        gst = (int(variant.price) * int(pro_qty)) * 0.05
        total = (int(variant.price) * int(pro_qty)) + 100 
        form = AddressForm()
        global context
        context = {
            'shipping_address':shipping_address,
            'variant':variant,
            'quantity':pro_qty,
            'gst':gst,
            'total':total + gst,
            'form':form,
            }

        return JsonResponse({'result':'successful'})
    else:
        return render(request,'checkout/checkout.html',context)



def order_invoice(request):
    return render(request,'checkout/invoice.html')


def add_address_checkout(request):
    address = User_Address.objects.filter(user=request.user)
    print('Iam penitrated here')
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect(checkout)
    else:
        form = AddressForm()

