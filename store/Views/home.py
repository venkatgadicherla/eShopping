from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
class Home(View):
    def post(self,request):
     
      product_id=request.POST.get('product_id')
      customer_id=request.POST.get('customer_id')
      remove=request.POST.get('remove')
      
       
      print(product_id,customer_id)
      cart=request.session.get('cart')
     
      if cart:
        print("cart ",cart)
        if(product_id):
          if(cart.get(product_id)):
            quantity=cart[product_id]
            if(remove):
               print('remove clicked the quantity is ',quantity)

               if quantity>1:
                 
                 quantity=quantity-1
                 print('after removal ',quantity)
                 cart[product_id]=quantity
                 request.session['cart']=cart
               elif quantity==1:
                 cart.pop(product_id)
                 request.session['cart']=cart
            else:
                 print('Product quantity',product_id," :",quantity)
                 cart[product_id]=quantity+1
                 request.session['cart']=cart
                 print('updated cart', request.session['cart'])
          else:
           
            print('new product to the cart id:',product_id)
            cart[product_id]=1
            request.session['cart']=cart
       
      else:
        
        cart={}
        cart[product_id]=1
        request.session['cart']=cart
      return redirect('/')
       
      
    def get(self,request):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
         products = Product.get_all_products_by_categoryid(categoryID)
        else:
         products = Product.get_all_products();
         data = {"products": products, "categories": categories}
        print('You are: ',request.session.get('customer_email'))
        return render(request, 'index.html', data)