from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from store.models import Customer,Product

class Cart(View):
    def get(self, request):
        if(request.session.get('customer')):
            ids=request.session.get('cart').keys()
            products = Product.get_products_by_id(ids)
            print(products)
            return render(request, 'cart.html',{'products':products})