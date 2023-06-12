from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib import messages
from django.views import View
class Logout(View):
    def post(self,request):
        request.session.flush()
        messages.success(request, "You are successfully logged out.")
        return redirect('/')
        