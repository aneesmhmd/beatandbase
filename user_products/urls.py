from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_products,name='user_products'),
    path('product_detail/<int:product_id>',views.product_detail,name='product_detail'),
    path('search_product',views.search_product,name='user_search_product'),
]
