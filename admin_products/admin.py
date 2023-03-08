from django.contrib import admin
from . import models

admin.site.register(models.Brand)
admin.site.register(models.Categories)
admin.site.register(models.Product)
admin.site.register(models.Product_Color)
admin.site.register(models.Product_Image)