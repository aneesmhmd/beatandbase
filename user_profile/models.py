from django.db import models
from user_home.models import CustomUser
import random

class User_Address(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    house_name = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)


    def __str__(self):
        return self.house_name
    



class Default_Address(models.Model):
    user = models.OneToOneField(CustomUser  , on_delete=models.CASCADE)
    default = models.OneToOneField(User_Address,on_delete=models.CASCADE)


def generate_order_id():
    """Generate a unique four-digit order ID."""
    while True:
        new_id = random.randint(1000, 9999)
        if not Product.objects.filter(product_id=new_id).exists():
            return new_id


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_id = models.IntegerField(unique=True, default=generate_order_id)