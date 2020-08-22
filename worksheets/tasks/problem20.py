# Problem 20 #Functions
# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi

print("""
  ***********************************************
  Okunusu bulmak

  Nedir?
  Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

  Press Q to quit
  ************************************************
""")

def okunusuBul(sayi):
  birlik = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
  ondalik = ['on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']

  okunus = ''
  if sayi[0]:
    okunus+=ondalik[int(sayi[0])-1]
  if sayi[1] == '0':
    return okunus
  if sayi[1]:
    okunus+=birlik[int(sayi[1])]
  return okunus

while True:
  sayi = input('Bir sayi giriniz:')
  if(sayi == 'q'):
    break
  print('Sayinizin okunusu:', okunusuBul(sayi))