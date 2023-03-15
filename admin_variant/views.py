from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product_Variant, Colors
from admin_products.models import Product

def product_variants(request):
    context = {
        'variants' : Product_Variant.objects.all().order_by('-product'),
        'products' : Product.objects.all().order_by('id'),
        'colors' : Colors.objects.all().order_by('id'),
    }
    return render(request,'admin_variant/product_variants.html',context)


def add_color(request):

    color = request.POST['color']
    Colors.objects.create(color_name = color)

    return redirect(product_variants)



def add_variant(request):
    product_id = request.POST['product']
    price = request.POST['price']
    color = request.POST['color']
    quantity = request.POST['quantity']

    # null value checking 
    check = [product_id,price,quantity]
    for values in check:
        if values == '':
            messages.info(request,'some fields are empty')
            return redirect(product_variants)
        else:
            pass
    
    # checking price and quantity is number
    try:
        check_number = int(price)
        check_number = int(quantity)
    except:
        messages.info(request,'number field got unexpected values')
        return redirect(product_variants)
    
    # checking price and quantity positive number
    check_pos =[int(price),int(quantity)]
    for value in check_pos:
        if value < 0:
            messages.info(request,'price and quantity should be positive number')
            return redirect(product_variants)
        else:
            pass
    
    
   
    product = Product.objects.get(id = product_id)
    color = Colors.objects.get(id=color)
    try:
        Product_Variant.objects.get(product=product,color=color)
    except:
        new = Product_Variant.objects.create(product=product,color=color, price=price, quantity=quantity)
        new.save()
    else:
        messages.info(request,f'{product} with {color} color already exist!')
    return redirect(product_variants)

def edit_variant(request,variant_id):
    product_id = request.POST['product']
    price = request.POST['price']
    color_id = request.POST['color']
    quantity = request.POST['quantity']

    check = [product_id,color_id,price,quantity]
    for values in check:
        if values == '':
            messages.info(request,'some fields are empty')
            return redirect(product_variants)
        else:
            pass
    
    try:
        check_number = int(price)
        check_number = int(quantity)
    except:
        messages.info(request,'number field got unexpected values')
        return redirect(product_variants)
   
    product = Product.objects.get(id = product_id)
    color = Colors.objects.get(id=color_id) 
    variant = Product_Variant.objects.filter(id=variant_id)
    variant.update(product=product,color=color, price=price, quantity=quantity)
    
    return redirect(product_variants)

def delete_variant(request):

    variant_id = request.GET.get('id')
    print(variant_id)
    variant = Product_Variant.objects.get(id= variant_id)
    variant.delete()

    return redirect(product_variants)
