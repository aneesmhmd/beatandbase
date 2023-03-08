from django.db import models
from admin_products.models import Product
from user_home.models import CustomUser

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.product) + ' by ' + str(self.user.username)