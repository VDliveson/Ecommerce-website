from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==int(product.id):
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return 0

@register.filter(name='cart_total')
def cart_total(cart):
    total_products=0
    keys=cart.keys()
    for id in keys:
        total_products+=1
    return total_products

@register.filter(name='price_total')
def price_total(products,cart):
    total_cost=0
    keys=cart.keys()
    sum=0
    for product in products:
        sum+=product_total(product,cart)
    return sum
        

@register.filter(name='product_total')
def product_total(product,cart):
    price=product.price
    keys=cart.keys()
    for id in keys:
       if int(id)==product.id:
            price=cart.get(id)*price;
    return price
            
            
    