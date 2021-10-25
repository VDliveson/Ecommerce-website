from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from store.models import Customer, Product, Order
from django.contrib import messages

class Checkout(View):
    def post(self, request):
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        street = request.POST.get('street')
        area = request.POST.get('area')
        city = request.POST.get('city')
        state = request.POST.get('state')
        full_address = str(street+' '+area+' '+city+' '+' '+state)
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          full_address=full_address,
                          quantity=cart.get(str(product.id)))

        order.placeOrder()
        request.session['cart']={}
        return redirect('cart')
