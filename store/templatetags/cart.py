from django import template

register= template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys: 
      if int(id) == product.id:
         return True
         
    return False
@register.filter(name='quantity_in_cart')
def quantity_in_cart(product,cart):
    keys=cart.keys()
    for id in keys: 
      if int(id) == product.id:
         return cart.get(id)
         
    return False
@register.filter(name='product_items_cost')
def product_items_cost(product,cart):
   quantity=quantity_in_cart(product,cart)
   cost=quantity*product.price
   return cost

@register.filter(name='cart_cost')
def cart_cost(products,cart):
   total=0
   for product in products:
      total+=product_items_cost(product,cart)
   return total