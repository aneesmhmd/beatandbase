from django.urls import path
from .views import *

urlpatterns = [

    #regarding with cart updations
    path('',cart_summary,name="cart-summary"),


    path('add',cart_add,name="cart-add"),


    path('delete',cart_delete,name="cart-delete"),


    path('update',cart_update,name="cart-update"),



    # regarding with quantity updations
    path('add_quantity',add_quantity,name="add-quantity"),


    # path('add_quantity',add_quantity,name="add-quantity"),

]
