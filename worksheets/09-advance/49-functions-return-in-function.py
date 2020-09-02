
#!Fonksiyonlar icinde return ile fonksiyon donderebiliriz asagidaki gibi

def anafonksiyon(islem):
  def toplama(*args):
    toplam = 0
    for i in args:
      toplam+=i
    return toplam

  def carpim(*args):
    carpim = 1
    for i in args:
      carpim *= i
    return carpim

  if islem == 'toplama':
    return toplama
  else:
    return carpim

fonk = anafonksiyon('toplama')
print(fonk(1,2,3,4,5,6,7)) #28

fonk2 = anafonksiyon('carpim')
print(fonk2(1,2,3)) #6

#######################
#! BASKA ORNEK

def toplama(a,b):
  return a+b
def cikarma(a,b):
  return a-b
def carpma(a,b):
  return a*b
def bolme(a,b):
  return a/b

def anafonksiyon(func1, func2, func3, func4, islem):
  if islem == 'toplama':
    print(func1(3,4))
  elif islem == 'cikarma':
    print(func2(10,3))
  elif islem == 'carpma':
    print(func3(3,5))
  elif islem == 'bolme':
    print(func4(10,4))
  else:
    print('Gecersiz islem')

anafonksiyon(toplama, cikarma, carpma, bolme, 'toplama') #7
anafonksiyon(toplama, cikarma, carpma, bolme, 'cikarma') #7
anafonksiyon(toplama, cikarma, carpma, bolme, 'carpma') #15
anafonksiyon(toplama, cikarma, carpma, bolme, 'bolme') #2.5
anafonksiyon(toplama, cikarma, carpma, bolme, 'asdasd') #Gecersiz islem