from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_orders',views.admin_orders,name='admin_orders'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
    path('admin_offers',views.admin_offers,name='admin_offers'),
]
