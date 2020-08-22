# Calculator #Modules
print("""
  ***********************************************
  Calculator Project

  Nedir?
  Kendinize ait gelismis bir hesap makinasi yapin

  1 Sum
  2 Minus
  3 Multiply
  4 Divide
  5 Square
  6 Cube
  7 SquareRoot
  8 Reset

  Press Q to quit
  ************************************************
""")

from methods import *


sonuc = 0
while True:
  process = input('Please choose a process here: ')
  if(input == 'q'):
    break

  if process == '1':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = sum(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '2':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = minus(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '3':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = multiply(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '4':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = divide(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '5':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = square(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '6':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = cube(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '7':
    sayi = int(input('Bir sayi giriniz: '))
    sonuc = squareRoot(sonuc, sayi)
    print(sonuc)
    continue
  elif process == '8':
    sonuc = 0
    print(sonuc)
    print('Hesap makinesi sifirlandi')
    continue
  else:
    print(sonuc)
    print('Gercersiz islem girdiniz lutfen tekrar deneyin')
    continue
