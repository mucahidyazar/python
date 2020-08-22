# Problem 17 #Functions
# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

print("""
  ***********************************************
  Mukemmel sayi bulma

  Nedir?
  Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

  Press Q to quit
  ************************************************
""")

def isPerfectNumber(number):
  toplam = 0
  for i in range(1,number):
    if (number % i == 0):
      toplam += i
  if (number == toplam):
    return True
  else:
    return False

while True:
  sayi = input('Bir sayi giriniz:')
  if(sayi == 'q'):
    break
  else:
    sayi = int(sayi)
    if(isPerfectNumber(sayi)):
      print('Sayi mukemmel bir sayidir')
    else:
      print('Sayi mukemmel bir sayi degildir')