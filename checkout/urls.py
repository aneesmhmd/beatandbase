from django.urls import path
from .views import *

urlpatterns = [
    path('',checkout,name='checkout'),
    path('invoice',order_invoice,name='invoice'),
    path('add_address',add_address_checkout,name='add_address_checkout'),
]
