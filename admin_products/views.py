from django.shortcuts import render,redirect
from .models import Product, Product_Image
from admin_brand.models import Brand
from admin_category.models import Categories
from django.http import JsonResponse
from django.contrib import messages


def admin_products(request):
    if request.method == 'POST':
        search_text = 'etd'
        context = {
            'products':Product.objects.filter(product_name__icontains=search_text),
            'categories':Categories.objects.all(),
            'brands':Brand.objects.all()
        }
    else:
        context = {
            'products':Product.objects.all().order_by('id'),
            'categories':Categories.objects.all(),
            'brands':Brand.objects.all(),
        }
    return render(request,'admin_products/admin_products.html',context)

def add_product(request):
    name = request.POST['product_name']
    brand = request.POST['product_brand']
    category = request.POST['product_category']
    price = request.POST['product_price']
    quantity = request.POST['product_quantity']

    check = [name,brand,category,price,quantity]
    for values in check:
        if values == '':
            messages.info(request,'some fields are empty')
            return redirect(admin_products)
        else:
            pass
    
    try:
        check_number = int(price)
        check_number = int(quantity)
    except:
        messages.info(request,'number field got unexpected values')
        return redirect(admin_products)
        

    image = request.FILES['image']
    brand_instance = Brand.objects.get(id=brand)
    category_instance = Categories.objects.get(id=category)
    new = Product.objects.create(is_available=True,product_img=image,product_name=name,brand=brand_instance,category=category_instance,product_price=price,product_quantity=quantity)
    new.save()
    return redirect(admin_products)

def edit_product(request,product_id):
    name = request.POST['product_name']
    price = request.POST['product_price']
    quantity = request.POST['product_quantity']
    brand = request.POST['product_brand']
    category = request.POST['product_category']
    try:
        product = Product.objects.get(id=product_id)
        image = request.FILES['image']
        product.product_img=image
        product.save()
    except:
        pass
    
    brand_instance = Brand.objects.get(id=brand)
    category_instance = Categories.objects.get(id=category)
    product = Product.objects.filter(id=product_id).update(product_name=name,brand=brand_instance,category=category_instance,product_price=price,product_quantity=quantity)
    mess_status = True
    return redirect(admin_products)

def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.info(request,f'deleted product "{product.product_name}"')
    return redirect(admin_products)

def upload_images(request):
    if request.method == 'POST':

        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=42)
        files = request.FILES.getlist('file')
        for file in files:
            pass
            image = Product_Image.objects.create(product = product,image=file)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    
# def del_multiple_images(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         image = Image.objects.get(id=id)
#         image.delete()
#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False})


def search_product(request):  
    search_text = request.POST['query']
    context = {
        'products':Product.objects.filter(product_name__icontains=search_text),
        'categories':Categories.objects.all(),
        'brands':Brand.objects.all()
    }
    return render(request,'admin_products/admin_products.html',context)