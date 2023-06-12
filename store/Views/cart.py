
from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models.product import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Cart(View):
    def get(self,request):
      product_list=list(request.session.get('cart').keys())
      products_data=Product.get_product_by_id(product_list)
      print('Products in Cart',products_data)
      return render(request,'cart.html',{'products':products_data})
    
    
   
    