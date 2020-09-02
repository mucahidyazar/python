def mukemmelDecorator(func):
  def wrapper(sayilar):
    mukemmelSayilar = []
    for x in sayilar:
      toplam = 0
      for y in range(1,x):
        if x % y == 0:
          toplam += y
      if toplam == x:
        mukemmelSayilar.append(x)
    print(mukemmelSayilar)
    
    func(sayilar)
  return wrapper


def isAsal(sayi):
  if(sayi == 1):
    return False
  elif (sayi == 2):
    return True
  else:
    for i in range(2, sayi):
      if(sayi % i == 0):
        return False
    return True

@mukemmelDecorator
def asalFunc(sayilar):
  asalSayilar = list()

  for x in sayilar:
    if isAsal(x):
      asalSayilar.append(x)
  print(asalSayilar)

asalFunc(range(2,1001))