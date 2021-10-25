from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models import Customer



class Signup(View):
    def get(self, request):
        customer=request.session.get('customer')
        if(customer):
            return redirect('home')
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        username = postData.get('username')
        email = postData.get('email')
        password = postData.get('password')
        password2 = postData.get('password2')
        number=postData.get('number')
        address=postData.get('address')
        
        
        val = {'username': username, 'email': email,
               'password': password, 'password2': password2,'number': number,'address': address}
        customer = Customer(username=username,
                            email=email, password=password,address=address,phone=number)

        if(isError(val, customer, request)):
            return render(request, 'signup.html')
        else:
            customer.password = make_password(password)
            customer.register()
            return redirect('home')


def isError(val, customer, request):
    if(val['username'] == '' or val['email'] == ''):
        messages.error(request, 'Empty fields.')
        return True

    elif(val['password'] == '' or val['password2'] == '' or val['password'] != val['password2']):
        messages.error(request, 'Passwords do not match.')
        return True

    elif(customer.is_Exists()):
        messages.error(request, 'Email already exists.')
        return True

    elif(val['number']):
        if(len(val['number'])!=10):
            messages.error(request, 'Invalid number.')
            return True
    else:
        return False
