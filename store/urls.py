"""
URL configuration for shoppingcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .Views.home import Home
from .Views.login import Login
from .Views.signup import Singup
from .Views.logout import Logout
from .Views.cart import Cart
urlpatterns = [
    path("", Home.as_view()),
    path('signup', Singup.as_view()),
    path('login',Login.as_view()),
    path('logout',Logout.as_view()),
    path('cart',Cart.as_view()),
   
  
   
]
