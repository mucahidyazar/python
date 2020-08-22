# Problem 18 #Functions
# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
# Problem için şu siteye bakabilirsiniz;
# http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

print("""
  ***********************************************
  EBOB bulma

  Nedir?
  Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini dönen bir tane fonksiyon yazın.

  Press Q to quit
  ************************************************
""")

def enBuyukOrtakBolen(sayi1, sayi2):
  sayi3 = 0
  sayi4 = 0
  if sayi1 > sayi2:
    sayi3 = sayi2
  if sayi1 < sayi2:
    sayi3 = sayi1
  for i in range(sayi3+1,1,-1):
    if (sayi1 % i == 0 and sayi2 % i ==0 and i > sayi4):
      sayi4 = i
  return sayi4

while True:
  sayi1 = input('Please write a nubmer for x:')
  sayi2 = input('Please write a nubmer for y:')
  if(sayi1 == 'q' or sayi2 == 'q'):
    break
  else:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    if(enBuyukOrtakBolen(sayi1, sayi2) == 0):
      print('Ortak bolen yoktur')
    else:
      print('En buyuk ortak bolen:',enBuyukOrtakBolen(sayi1, sayi2))
    
      


