from django.db import models
from user_home.models import CustomUser
from user_profile.models import User_Address
from admin_variant.models import Product_Variant
import string
import random
from datetime import datetime



def generate_order_id():
    """Generate a 14-character order ID"""
    while True:
        letters = string.ascii_uppercase + string.digits
        order_id = ''.join(random.choice(letters) for i in range(9))
        year = str(datetime.now().year)[-2:]
        month = str(datetime.now().month)[-2:]
        day = str(datetime.now().day)
        hour = str(datetime.now().hour)
        new_id = 'BNB' + month + day + hour+ order_id
        return new_id

class Payment_methods(models.Model):
    method = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.method
        
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    order_id = models.CharField(max_length=20, default=generate_order_id, unique=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,null=True)
    address = models.ForeignKey(User_Address, on_delete=models.SET_NULL,null=True)
    placed_at = models.DateTimeField(auto_now_add=True,null=True)
    gst = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    payment_method = models.ForeignKey(Payment_methods,on_delete=models.SET_NULL,null=True)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    payment_order_id = models.CharField(max_length=100,null=True,blank=True)
    payment_signature = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self) -> str:
        return self.order_id


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    variant = models.ForeignKey(Product_Variant, on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField()

    def get_total(self):
        self.variant.price * self.quantity

    

