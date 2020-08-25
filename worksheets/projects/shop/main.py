print("""
  Welcome to Computer Shop
  1 Buy Computer
  2 Buy CPU
  3 Buy Motherboard
  4 Buy SSD
  5 Buy Gpu
  6 Buy Memory
  7 Buy Power
  8 Your Basket
  9 Your Orders
  10 Working Hours   

  Press Q to exit
""")

import json
from computer import Computer
from client import Client

with open('stocks.json', 'r', encoding='utf-8') as stocks:
  data = json.load(stocks)

yourName = input('What is your name : ')
yourWallet = int(input('What is your wallet balance : '))
client = Client(yourName, yourWallet)

def add(select):
  if select:
    # if client.wallet < select['price']:
    #   print('You money is not enough for this')
    client.wallet -= select['price']
    # print("""
    #   {}$ were spent
    #   Your wallet => {}

    #   What do you want now?      
    #   1 Buy again
    #   2 Menu

    #   Press Q to exit
    # """.format(select['price'], client.wallet))
    piece = int(input('How many items do you want to add? #'))
    client.addToCart({
      "product": select,
      "piece": piece
    })
    # navigate = input('#')
    # if navigate == '1':
    #   add(select)
    # elif navigate == '2':
    #   pass
    # else:
    #   print('Wrong choose')
  else:
    print('You have chosed wrong option')  

while True:
  process = input('Please choose a option : ')

  if process == 'q':
    break

  if process == '2':
    for x in data['cpu']:
      print(x['id'], x['brand']+' '+x['model']+' '+str(x['cores'])+' Cores '+x['socket'], x['price'])
    select = input('Which product do you want to add? #')
    add(data['cpu'][int(select)-1])

  if process == '3':
    for x in data['motherboard']:
      print(x['id'], x['brand']+' '+x['model']+' '+x['socket']+' '+x['type'], x['price'])
    select = input('Which product do you want to add? #')
    add(data['motherboard'][int(select)-1])

  if process == '4':
    for x in data['ssd']:
      print(x['id'], x['brand']+' '+x['model']+' '+str(x['capacity'])+'GB', x['price'])
    select = input('Which product do you want to add? #')
    add(data['ssd'][int(select)-1])

  if process == '5':
    for x in data['gpu']:
      print(x['id'], x['brand']+' '+x['model']+' '+str(x['memory'])+' GB '+str(x['bit'])+'bit '+str(x['clock-speed'])+'Ghz ', x['price'])
    select = input('Which product do you want to add? #')
    add(data['gpu'][int(select)-1])

  if process == '6':
    for x in data['memory']:
      print(x['id'], x['brand']+' '+x['model']+' '+str(x['memory']/x['piece'])+'x'+str(x['piece'])+'GB '+x['type']+' '+str(x['speed'])+'Mhz', x['price'])
    select = input('Which product do you want to add? #')
    add(data['memory'][int(select)-1])

  if process == '7':
    for x in data['power']:
      print(x['id'], x['brand']+' '+x['model']+' '+str(x['power'])+'W', x['price'])
    select = input('Which product do you want to add? #')
    add(data['power'][int(select)-1])

  if process == '8':
    client.showBasket()
    navigate = input("""
      What do you want to do?

      1 Buy
      2 Clear Your Basket
      3 Menu
    """)

    if navigate == "1":
      client.buy()
    elif navigate == "2":
      client.clear()
    elif navigate == "3":
      continue
    else:
      print('You chosed wrong option')

  if process == '9':
    client.showOrders()
      

