
from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Login(View):
    def get(self,request):
      return render(request,'login.html')
    
    
    def post(self,request):
    
        emailid = request.POST.get('email')
        password = request.POST.get('password')
       # print(emailid,password)
        customer = Customer.getCustomer(emailid)
        if customer:
           print(customer.email)
           if(check_password(password,customer.password)): 
              request.session['customer_id']=customer.id
              request.session['customer_email']=customer.email
               
              return redirect('/')
           else:
             messages.success(request,("There was error while logging in.Please check ur username or password"))
             return redirect('/login')
        else:
            messages.success(request,("There was error while logging in.Please check ur username or password"))
            return redirect('/login')
    