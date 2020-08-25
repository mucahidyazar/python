from functools import reduce
import random

class Client():
  def __init__(self, name, wallet):
    self.name = name
    self.wallet = wallet
    self.cart = []
    self.orders = []

  def addToCart(self, item):
    self.cart.append(item)

  def showBasket(self):
    for item in self.cart:
      print(item)

  def buy(self):
    total = 0
    for x in self.cart:
      total += x['product']['price'] * x['piece']
    if self.wallet > total:
      self.orders.append({
        'id': random.randint,
        'products': self.cart
      })
      self.cart = []
      print('You ordered successfully')
    else:
      print('Your money is not enought for this basket')

  def clear(self):
    self.cart = []
    print('Your basket were cleared')

  def showOrders(self):
    for order in self.orders:
      print(order, '\n')

  def __str__(self):
    print("""
      The products in your cart:
    """)

  def __len__(self):
    return len(self.cart)