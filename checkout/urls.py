from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/<int:item_id>',checkout,name='checkout'),
    path('invoice',order_invoice,name='invoice'),
]
