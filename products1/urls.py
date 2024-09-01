from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('product_List',views.show_products,name='products1'),
    path('signup_view',views.signup_view,name='signup_view'),
    path('login_view',views.login_view,name='login_view'),
]