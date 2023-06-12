
from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class Singup(View):
 def validate_form(self,form_data):
    customer = Customer(first_name=form_data['first_name'], last_name=form_data['last_name'], phone=form_data['phone'],
                            email=form_data['email'], password=make_password(form_data['password1']))
    print(customer.first_name)
    error_message=''
    if not form_data['first_name']:
        error_message='Please Enter a valid first name'
    elif len(form_data['first_name'])<4:
          error_message='Please Enter a valid first name'
    elif not form_data['last_name']:
        error_message='Please Enter a valid last name'
    elif len(form_data['last_name'])<4:
          error_message='Please Enter a valid last name'
    elif not form_data['phone']:
        error_message='Please Enter a valid '
    elif len(form_data['phone'])<10:
          error_message='Please Enter a valid phone no'
    elif not form_data['password1']:
        error_message='Please Enter a valid password 1'
    elif len(form_data['password1'])<5:
          error_message='Please Enter a valid password 1.1'
    elif not form_data['password2']:
        error_message='Please Enter a valid password 2'
    elif len(form_data['password2'])<5:
          error_message='Please Enter a valid password 2.1'
    elif form_data['password1']!=form_data['password2']:
        error_message="Passwords do not match"
    elif customer.isExists():
        error_message="Email already registered."
    return customer,error_message
 
 def get(self,request):
     
       
      return render(request, 'signup.html')
 def post(self,request):
   
        postdata = request.POST
        form_data={ "first_name" : postdata.get("firstname"),
        "last_name" : postdata.get('lastname'),
        "phone" : postdata.get('phone'),
        "email": postdata.get('email'),
        "password1" : postdata.get("password1"),
        "password2" : postdata.get("password2"),
        }
        customer, error_message = self.validate_form(form_data)
        
        if not error_message:

        
         customer.register()
         return redirect('/login')
        else: 
            send_data={"error":error_message,"data":form_data}
            return render(request,'signup.html',send_data)
            
   

