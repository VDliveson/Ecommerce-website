from django import template

register = template.Library()

@register.filter(name='total_price_order')
def total_price_order(price,quantity):
    return price*quantity


# @register.filter(name='total_order')
# def total_order(orders):
#     sum=0
#     for order in orders:
#         sum+=total_price_order(order.product.price,order.quantity)
#     return sum
    