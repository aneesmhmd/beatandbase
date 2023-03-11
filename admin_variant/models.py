from django.db import models
from admin_products.models import Product
# Create your models here.

class Colors(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name
    

class Product_Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(blank=True)
    price = models.PositiveIntegerField(null=True)
    is_available = models.BooleanField(default=True,blank=True)

    def __str__(self) -> str:
        return str(self.product) + ' with ' + str(self.color) +  ' color'