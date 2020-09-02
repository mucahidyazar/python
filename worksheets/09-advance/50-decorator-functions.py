#Kod tekrarini engeller
#dinamik ekstra ozellikler eklememizi saglarlar

#!TIME ILE ZAMAN HESAPLAMAK
import time

def karaleriHesapla(sayilar):
  sonuc = list()
  baslama = time.time()
  for i in sayilar:
    sonuc.append(i**2)
  bitis = time.time()
  print('Bu fonksiyon '+ str(bitis-baslama)+' saniye surdu')
  return sonuc

def kupleriHesapla(sayilar):
  sonuc = list()
  baslama = time.time()
  for i in sayilar:
    sonuc.append(i**3)
  bitis = time.time()
  print('Bu fonksiyon '+ str(bitis-baslama)+' saniye surdu')
  return sonuc

karaleriHesapla(range(100000))
kupleriHesapla(range(100000))


#!DECORATOR ILE AYNI ISLEMI YAPMAK
import time

#!Decorator functionumuzu bu sekilde burada tanimlariz
def zamanHesapla(func):
  def wrapper(sayilar):
    baslama = time.time()
    sonuc = func(sayilar) #Normal fonksiyonu calistirir
    bitis = time.time()
    print(func.__name__ + ' ' + str(bitis-baslama) + ' saniye surdu')
    return sonuc
  return wrapper

#! DECORATOR etmek istedigimiz functionun ustune decorator tanimimizi 
#!bu sekilde ekleyecegimiz fonksiyonlarin uzerine bu sekilde tanimlariz
@zamanHesapla 
def karaleriHesapla(sayilar):
  sonuc = list()
  for i in sayilar:
    sonuc.append(i**2)
  return sonuc

@zamanHesapla
def kupleriHesapla(sayilar):
  sonuc = list()
  for i in sayilar:
    sonuc.append(i**3)
  return sonuc

karaleriHesapla(range(100000))
kupleriHesapla(range(100000))
# karaleriHesapla 0.02293705940246582 saniye surdu
# kupleriHesapla 0.024965286254882812 saniye surdu

#!DETAYLI ANLATIM
#python ilk once calistirilan fonksiyon karaleriHesapla'yi bulur
#ve calistirilirken @zamanHesaplayi gorur ve altindaki functionu alarak
#zamanHesapla decoratoruna goturur ve onun argumenti olarak
#bu functionu tanimlar. karaleriHesapla fonksiyonuyla gonderilen
#argumentleride zamanHesaplayi fonksiyonu icindeki wrapper functionu icin
#argument olarak verir ve hesaplama bu sekilde baslar ve biter


###
#!BASKA ORNEK
###
def ekstra(fonk):
  def wrapper(sayilar):
    ciftlerToplami = 0
    ciftSayilar = 0
    teklerToplami = 0
    tekSayilar = 0
  
    for sayi in sayilar:
      if sayi % 2 == 0:
        ciftlerToplami += sayi
        ciftSayilar += 1
      else:
        teklerToplami += sayi
        tekSayilar += 1
    print('Teklerin ortalamasi :',teklerToplami / tekSayilar)
    print('Ciftlerin ortalamasi :',ciftlerToplami / ciftSayilar)

    #Normal icine aldigi fonksiyonu calistirir
    #Yukaridakileri ise ekstra yapar
    fonk(sayilar) 
  return wrapper

@ekstra
def ortalamaBul(sayilar):
  toplam = 0
  for sayi in sayilar:
    toplam += sayi
  print('Genel ortalama :', toplam/len(sayilar))

ortalamaBul([1,2,3,4,65,84,5,32]) #24.5

# Teklerin ortalamasi : 18.5
# Ciftlerin ortalamasi : 30.5
# Genel ortalama : 24.5