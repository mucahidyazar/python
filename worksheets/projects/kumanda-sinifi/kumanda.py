import random
import time

class Kumanda():

  def __init__(self,tvDurum = 'Kapali',tvSes = 0, kanalListesi = ['trt'], kanal='trt'):
    self.tvDurum = tvDurum
    self.tvSes = tvSes
    self.kanalListesi = kanalListesi
    self.kanal = kanal

  def tvAc(self):
    if(self.tvDurum == 'Acik'):
      print('Tv zaten acik')
    else:
      print('Tv aciliyor')
      self.tvDurum = 'Acik'

  def tvKapat(self):
    if(self.tvDurum == 'Kapali'):
      print('Tv zaten kapali')
    else:
      print('Tv kapaniyor')
      self.tvDurum = 'Kapali'

  def sesAyarlari(self):
    while True:
      cevap = input("Sesi Azalt: '<'\nSesi Arttir: '>'\nCikis: 'q' ")
      if(cevap == '<'):
        if(self.tvSes != 0):
          self.tvSes -= 1
          print('Ses', self.tvSes)
      elif(cevap == '>'):
        if(self.tvSes != 31):
          self.tvSes += 1
          print('Ses', self.tvSes)
      else:
        print('Ses guncellendi', self.tvSes)
        break

  def kanalEkle(self, kanalIsmi):
    print('Kanal ekleniyor...')
    time.sleep(1)
    self.kanalListesi.append(kanalIsmi)
    print('Kanal eklendi...')

  def rastgeleKanal(self):
    rastgele = random.randint(0,len(self.kanalListesi-1))
    self.kanal = self.kanalListesi[rastgele]
    print('Suanki kanal :', self.kanal)

  def __len__(self):
    return len(self.kanalListesi)

  def __str__(self):
    return 'Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nSuanki Kanal: {}\n'.format(self.tvDurum, self.tvSes, self.kanalListesi, self.kanal)

kumanda = Kumanda()

print("""
  Televizyon Uygulamasi

  1 Tv Ac
  2 Tv Kapat
  3 Ses Ayarlari
  4 Kanal Ekle
  5 Kanal Sayisini Ogrenme
  6 Rastgele Kanal
  7 TV Bilgileri
  
  Cikmak icin Q ya basin
""")

while True:
  islem input('Islemi seciniz :')

  if(islem == 'q'):
    print('Program sonlandiriliyor...')
    break

  elif(islem == '1'):
    kumanda.tvAc()
  elif(islem == '2'):
    kumanda.tvKapat()
  elif(islem == '3'):
    kumanda.sesAyarlari()
  elif(islem == '4'):
    kanalIsimleri = input("Kanal isimlerini ',' ile ayirarak giriniz:")
    kanalListesi = kanalIsimleri.split(',') 

    for eklenecekler in kanalListesi:
      kumanda.kanalEkle(eklenecekler)
  elif(islem == '5'):
    print('Kanal Sayisi:', len(kumanda)) #__len__ calisacak
  elif(islem == '6'):
    kumanda.rastgeleKanal()
  elif(islem == '7'):
    print(kumanda) #__str__ calisacak
  else:
    print('Gecersiz islem...')
      


