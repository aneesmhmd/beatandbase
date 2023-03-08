from django.urls import path
from .views import *

urlpatterns = [
    path('',wishlist,name='wishlist'),
    path('add/<int:product_id>',add_wishlist,name='add-wishlist'),
    path('delete/<int:product_id>',delete_wishlist,name='delete-wishlist')
]
