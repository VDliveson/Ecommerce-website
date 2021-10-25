from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models import Customer



class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if(email == '' or password == ''):
            messages.error(request, 'Empty fields')
            return render(request, 'login.html')

        customer = Customer.get_Customer(email)

        if customer:
            flag = check_password(password, customer.password)

            if flag:
                request.session['customer'] = customer.id
                return redirect('home')
            else:
                messages.error(request, 'Password not found')

        else:
            messages.error(request, 'User does not exists')
        return render(request, 'login.html')


def logout(request):
    messages.success(request, 'User logged out successfully')
    request.session.clear()
    return redirect('login')
