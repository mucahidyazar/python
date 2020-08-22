
#! Inheritance bir sinifin baska bir siniftan ozelliklerini almasidir. 
#! Javascript class yapisindaki extends kullanimi gibi

class Calisan():

  def __init__(self, isim, maas, departman):
    print('Calisan sinifinin init fonksiyonu')
    self.isim = isim
    self.maas = maas
    self.departman = departman

  def bilgileriGoster(self):
    print("""
      Calisan sinifinin bilgileri
      Isim: {}
      Maas: {}
      Departman: {}
    """.format(self.isim, self.maas, self.departman))

  def departmanDegistir(self, yeniDepartman):
    self.departman = yeniDepartman

#Yonetici sinifinin Calisan sinifindaki ozellikleri inheritance olarak almasi icin
#tek yapmamiz gereken Yonetici sinifini tanimlarken parantez icine inheritance
#almak istedigi sinifi tanimlamamizdir.
#*pass => Sinifi bos tanimlamak sitedigimiz zaman yazariz. Yazmaz ve bos birakirsak hata aliriz
class Yonetici(Calisan):
  
  def zamYap(self, miktar):
    self.maas += miktar

yonetici = Yonetici('Mustaafa Aral', 3000, 'Bilisim')
yonetici.bilgileriGoster()
      # Calisan sinifinin bilgileri
      # Isim: Mustaafa Aral
      # Maas: 3000
      # Departman: Bilisim
yonetici.departmanDegistir('IT')
yonetici.bilgileriGoster()
      # Calisan sinifinin bilgileri
      # Isim: Mustaafa Aral
      # Maas: 3000
      # Departman: IT
yonetici.zamYap(2000)
yonetici.bilgileriGoster()
      # Calisan sinifinin bilgileri
      # Isim: Mustaafa Aral
      # Maas: 5000
      # Departman: IT

#! Overwriting => Miras aldigimiz class sinifindaki metodlardan birisiyle ayni 
#! isimde metod tanimlarsak miras aldigimiz degil kendi metodumuz calisiyor.
class Calisan1():

  def __init__(self, isim, maas, departman):
    print('Calisan sinifinin init fonksiyonu')
    self.isim = isim
    self.maas = maas
    self.departman = departman

  def zamYap(self, miktar):
    self.maas += miktar

class Yonetici1(Calisan):
  #! Buraya yeni birsey ekleyip overwrite etmekde bu sekilde oluyor
  def __init__(self, isim, maas, departman, kisiSayisi):
    print('Yonetici sinifinin init fonksiyonu')
    self.isim = isim
    self.maas = maas
    self.departman = departman
    self.kisiSayisi = kisiSayisi

  #! zampYap metodumuzu overwrite yapmis oluyoruz boylelikle
  def zamYap(self, miktar):
    self.maas += miktar*2

newYonetici = Yonetici1('Oguz Hakan', 3500, 'Bilisim', 10)
print(newYonetici.maas) #3500
newYonetici.zamYap(200)
print(newYonetici.maas) #3900

###!
#! SUPER anahtar kelimesi
###!
class Calisan2():

  def __init__(self, isim, maas, departman):
    print('Calisan sinifinin init fonksiyonu')
    self.isim = isim
    self.maas = maas
    self.departman = departman

  def zamYap(self, miktar):
    self.maas += miktar

class Yonetici2(Calisan):
  #! Yukarida SUPER kullanmadan inheritancedeki kodlari tekrar ederek bu kismi yapmistik
  #! Simdi SUPER ile yukaridaki kod tekrarini ortadan kaldiracagiz
  #! kendi __init__ metodumuz icinde super() i cagiriyoruz ve bu bizi inheritance classina baglayacak
  #! ve ve inheritance deki __init__ metoduna baglaniyoruz ve isine kendi __init__ metodumuzdan gelen degerleri vererek kisa yoldan tum yukaridaki uzun tanimlamalardan kurtuluyoruz.
  def __init__(self, isim, maas, departman, kisiSayisi):
    super().__init__(isim, maas, departman)
    print('Yonetici sinifinin init fonksiyonu')
    self.kisiSayisi = kisiSayisi

  #! zampYap metodumuzu overwrite yapmis oluyoruz boylelikle
  def zamYap(self, miktar):
    self.maas += miktar*2