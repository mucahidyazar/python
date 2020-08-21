# Problem 7
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
# BKİ 18.5'un altındaysa -------> Zayıf
# BKİ 18.5 ile 25 arasındaysa ------> Normal
# BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
# BKİ 30'un üstündeyse -------------> Obez

boy = int(input('Boy: ')) / 100
kilo = int(input('Kilo: '))
bki = kilo / (boy * boy) #Beden Kitle Indeksi => Kilo / Boy(m) * Boy(m)

if bki < 18.5:
  print('Zayif')
elif bki < 25:
  print('Normal')
elif bki < 30:
  print('Fazla kilolu')
elif bki > 30:
  print('Obez')
else:
  print('Gecersiz islem')