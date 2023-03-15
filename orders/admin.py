from django.contrib import admin
from .models import Order,Order_item,Payment_methods

admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Payment_methods)
