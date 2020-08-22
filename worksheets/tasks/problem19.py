# Problem 19 #Functions
# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
# Problem için şu siteye bakabilirsiniz;
# http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

print("""
  ***********************************************
  Mukemmel sayi bulma

  Nedir?
  Kullanıcıdan 2 tane sayı alarak bu sayıların en kucuk ortak bölenini dönen bir tane fonksiyon yazın.

  Press Q to quit
  ************************************************
""")

def enKucukOrtakBolen(sayi1, sayi2):
  enKucukSayi = 0
  enKucukOrtakBolen = 1
  if(sayi1 < sayi2):
    enKucukSayi = sayi1
  elif(sayi1 == sayi2):
    enKucukSayi = sayi1
  else:
    enKucukSayi = sayi2
  
  for i in range(1,enKucukSayi):
    if(sayi1 % i == 0 and sayi2 % i == 0):
      enKucukOrtakBolen = i
  return enKucukOrtakBolen

while True:
  sayi1 = input('Lutfen birinci sayiyi yaziniz:')
  sayi2 = input('Lutfen ikinci sayiyi yaziniz:')
  if(sayi1 == 'q' or sayi2 == 'q'):
    break
  else:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print('En kucuk ortak bolen:', enKucukOrtakBolen(sayi1, sayi2))