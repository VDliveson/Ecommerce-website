from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models import *

class Index(View):
    def post(self, request):
        customer=request.session.get('customer')
        product= request.POST.get('product')
        cart=request.session.get('cart')
        remove=request.POST.get('remove')
        if (not customer):
            messages.error(request, 'Kindly login to continue')
            return redirect('login')
        if cart:
            quantity= cart.get(product)
            if quantity:
                if remove:
                    if(quantity<=1):
                        cart.pop(product)
                    else:
                        cart[product] =quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart ={}
            cart[product]=1
            
        request.session['cart']=cart
        return redirect('home')

    def get(self, request):
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if(category_id):
            products = Product.get_all_products_by_id(category_id)
        else:
            products = Product.get_all_products()

        return render(request, 'index.html', {'products': products, 'categories': categories})


def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")