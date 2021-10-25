from django.urls import path
from . views import *



urlpatterns = [
    path('',home.Index.as_view(),name='home'),
    path('signup',signup.Signup.as_view(),name='signup'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('checkout',checkout.Checkout.as_view(),name='checkout'),
    path('clear_session', home.delete_session)
    
]