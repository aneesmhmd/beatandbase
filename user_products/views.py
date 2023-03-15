from django.shortcuts import render,redirect
from ad_banner.models import Advertisement
from admin_products import models as admin_products
from admin_products.models import Product_Image 
from django.http import JsonResponse
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from admin_variant.models import Product_Variant 

def user_products(request):

    products = admin_products.Product.objects.all().order_by('product_name')
    
 
    sort_by = request.GET.get('sort_by')

    
    if sort_by == 'name_a_to_z':
        products = products.order_by('product_name')
    elif sort_by == 'name_z_to_a':
        products = products.order_by('-product_name')
    
    paginator = Paginator(products,6)
    page_number = request.GET.get('page')
    page_product = paginator.get_page(page_number)

    

    dicts = {
        'categories': admin_products.Categories.objects.all().order_by('id'),
        'brands': admin_products.Brand.objects.all().order_by('id'),
        'ad':Advertisement.objects.all().order_by('id'),
        'product':page_product,
        'variants':Product_Variant.objects.all(),
    }
    return render(request,'user_products/user_products.html',dicts)



def search_product(request):

    try:
        search_text = request.POST['search_text']
    except:
        return redirect(user_products)

    dicts = {
        'categories': admin_products.Categories.objects.all(),
        'product':admin_products.Product.objects.filter(product_name__icontains=search_text),
        'search_text' : search_text
    }
    return render(request,'user_products/product_search.html',dicts)

def product_detail(request,product_id):
    pro_images = ''
    mainproduct = admin_products.Product.objects.get(id=product_id)
    # pro_category = main_product.category
    # pro_category
    pro_images = Product_Image.objects.filter(product=product_id)

    dicts = {
        'variants':Product_Variant.objects.filter(product=mainproduct),
        'categories': admin_products.Categories.objects.all(),
        'ad':Advertisement.objects.all(),
        'm_product':mainproduct,
        'products':admin_products.Product.objects.all(),
        'checkout_qty':'checkout_qty',
        'images':pro_images
    }
    return render(request,'user_products/detail.html',dicts)