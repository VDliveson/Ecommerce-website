from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from store.models import Customer, Product, Order
from django.contrib import messages
from django.utils.decorators import method_decorator
from store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self,request):
        if(request.session.get('customer')):
            customer =request.session.get('customer')
            orders=Order.get_orders_by_customer(customer)
            return render(request,'orders.html',{'orders':orders})
        else:
            messages.info(request,'No active user found')
            return redirect('login')
        
    
    