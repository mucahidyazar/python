import time
import random

class Computer():
  def __init__(
    self,
    users = [{
      "username": "admin",
      "password": "admin"
    }], 
    power = False, 
    cpu = [
      { 'brand':'Intel', 'model':'6700K', 'price':199.10 }
      { 'brand':'Intel', 'model':'6500K', 'price':149.99 }
      { 'brand':'Intel', 'model':'6300K', 'price':99 }
    ], 
    ram = [
      { 'brand':'Corsair', 'type':'DDR4', 'memory':16, 'price':99.50 },
      { 'brand':'Ballistix', 'type':'DDR4', 'memory':16, 'price':89.99 },
      { 'brand':'Kingston', 'type':'DDR4', 'memory':16, 'price':74.99 },
      { 'brand':'Corsair', 'type':'DDR4', 'memory':8, 'price':90 },
      { 'brand':'Ballistix', 'type':'DDR4', 'memory':8, 'price':74.99 },
      { 'brand':'Kingston', 'type':'DDR4', 'memory':8, 'price':60 }
    ],
    ssd = [
      { 'brand':'Samsung', 'memory':250, 'price':31.99 },
      { 'brand':'Samsung', 'memory':500, 'price':59.99 },
      { 'brand':'Samsung', 'memory':1000, 'price':149.50 },
      { 'brand':'ADATA', 'memory':250, 'price':26.99 },
      { 'brand':'ADATA', 'memory':500, 'price':49.99 },
      { 'brand':'ADATA', 'memory':1000, 'price':109.50 },
    ],
    gpu = [
      { 'brand': 'Nvidia', 'model': 'RTX 2080', 'memory': 24, 'price': 1999.99 },
      { 'brand': 'Nvidia', 'model': 'RTX', 'memory': 12, 'price': 1349.99 },
      { 'brand': 'Nvidia', 'model': 'RTX', 'memory': 10, 'price': 849.99 },
      { 'brand': 'Nvidia', 'model': 'RTX', 'memory': 8, 'price': 599.99 },
      { 'brand': 'Nvidia', 'model': 'RTX', 'memory': 11, 'price':  },
      { 'brand': 'Nvidia', 'model': 'RTX', 'memory': 8, 'price': 2000 },
      { 'brand': 'Nvidia', 'model': 'RTX', 'memory': 6, 'price': 2000 },
      { 'brand': 'Nvidia', 'model': 'GTX', 'memory': 8, 'price': 2000 },
      { 'brand': 'Nvidia', 'model': 'GTX', 'memory': 8, 'price': 2000 },
      { 'brand': 'Nvidia', 'model': 'GTX', 'memory': 6, 'price': 2000 },
    ],
    powerSupply = {
      'brand': 'Evga',
      'model': '750P2'
    },
    total: 0,
    paid: False
  ):
    self.users = users
    self.power = power
    self.cpu = cpu
    self.ram = ram
    self.ssd = ssd
    self.gpu = gpu
    self.powerSupply = powerSupply
  
  def __str__(self):
    print("""
      Computer Information:
      Power: {}
        CPU: {}
        RAM: {}
        GPU: {}
        SSD: {}
        POWER SUPPLY: {}
    """.format(self.power, self.cpu, self.ram, self.gpu, self.ssd, self.powerSupply))

  def __len__(self):
    return len(self.users)

  def powerOn(self):
    print('Computer is turning on...')
    time.sleep(1)
    self.power = True
    print('Please login your account')
    username = input('Username : ')
    password = input('Password : ')
    user = { 'username': '', 'password': '' }
    for info in self.users:
    #   print(type(info))
      if info['username'] == username:
        user = info
        break
    if(password == user['password']):
      print('You are logged in succesfully')
    else:
      print('Username or password is wrong!')

  def powerOff(self):
    print('Computer is turning off...')
    time.sleep(1)
    self.power = False
    print('Computer is closed')

  def addMoreRam(self):
    ram = int(input('How many GB ram will you add : '))
    self.ram += ram
    print('You added {}GB DDR4 RAM'.format(ram))

  def addMoreSsd(self):
    ssd = int(input('How many GB ssd do you want add : '))
    self.ssd += ssd
    print('You added {}GB SSD'.format(ssd))


computer = Computer()

computer.powerOn()