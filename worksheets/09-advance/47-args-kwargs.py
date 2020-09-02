
#!ARGS
#Esnek sayida yani diledigimiz kadar argumen gondermemize yarar ve daha sonra bunlari args ile TUPLE halinde yakalariz
def fonksiyon(*args):
  for i in args:
    print(i)

#Fonksiyon icine gonderdigimiz argumentler *args ile demet haline donusur ve uzerinde dolasabiliriz
fonksiyon(1,2,3)
#1
#2
#3

def fonksiyon(isim, *args):
  print(isim)
  print('---------')
  for i in args:
    print(i)

fonksiyon('Murat',1,2,3,4)
# Murat
# ---------
# 1
# 2
# 3
# 4

#!KWARGS => ARGUMENTS lere KEY DEGERI VEREREK GONDERMEK ve DICTIONARY ALMAK
def fonksiyon(**kwargs):
  print(kwargs)

fonksiyon(isim = 'Murat', soyisim = 'Coskun', numara = 12345)
#{'isim': 'Murat', 'soyisim': 'Coskun', 'numara': 12345}

def fonksiyon(**kwargs):
  for x,y in kwargs.items():
    print('Key =>', x, 'Value =>',y)
fonksiyon(isim = 'Murat', soyisim = 'Coskun', numara = 12345)
# Key => isim Value => Murat
# Key => soyisim Value => Coskun
# Key => numara Value => 12345

def fonksiyon(*args, **kwargs):
  for i in args:
    print(i)
  print('----------')
  for i,j in kwargs.items():
    print(i,j)
fonksiyon() #
fonksiyon(1,2,3,4,5,isim = 'Murat', soyisim = 'Coskun', numara = 12345)
# 1
# 2
# 3
# 4
# 5
# ----------
# isim Murat
# soyisim Coskun
# numara 12345

