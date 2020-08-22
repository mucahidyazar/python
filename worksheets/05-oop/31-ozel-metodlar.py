# Nesne leri olusturdugumuzda Python tarafindan olusturdugumuz nesnelere ozel olarak
#Python tarafindan ozel olarak olusturulan metodlardir. Bunlarin bazilarini
#bizim kendimiz duzenlememiz gerekebiliyor bazen. Example: __init__

class Kitap1():
  pass

#kitap = Kitap1() # __init__ #Python cagirmaya calisir
#__init__ calisir ilk basta bos gibi birsey oldugu icin bir sonuc yazdirilmaz

#print(kitap) # __str__ #Python cagirmaya calisir
#<__main__.Kitap1 object at 0x000002095CCA49A0>

#len(kitap) # __len__ #Python cagirmaya calisir
#TypeError: object of type 'Kitap1' has no len()

#del kitap # __del__ Python cagirmaya calisir
#kitabi siler

class Kitap2():
  def __init__(self, isim, yazar, sayfaSayisi, tur):
    print('Kitap init fonksiyonu')
    self.isim = isim
    self.yazar = yazar
    self.sayfaSayisi = sayfaSayisi
    self.tur = tur

  #bu __str__ metodu aslinda print ile objemizi yazdirdigimizda cagrilacak metoddur.
  #yukarida orjinal hali var eger hic mduahale etmezsek oradaki gibi cikti verir
  #burada ise biz kendimize gore sekil veriyoruz
  def __str__(self):
    return 'Isim: {}\nYazar: {}\nSayfa sayisi: {}\nTuru: {}'.format(self.isim, self.yazar, self.sayfaSayisi, self.tur)

  def __len__(self):
    return self.sayfaSayisi

  def __del__(self):
    #Burada del metodunu yeniden tanimlamiyoruz aslinda bu mumkun degil del metodu icin
    #Burada phyton un del ine ekstra ozellikler ekliyoruz. Yani silinirken calismasi gereken diger ozellikleri ekliyoruz
    print('Kitap ogesi siliniyor')

kitap = Kitap2('Istanbul hatirasi', 'Ahmet Umit', 561, 'Polisiye')
  # __init__ => Kitap init fonksiyonu
print(kitap)
  #bu __str__ metodu aslinda print ile objemizi yazdirdigimizda cagrilacak metoddur.
  #yukarida orjinal hali var eger hic mduahale etmezsek oradaki gibi cikti verir
  #burada ise biz kendimize gore sekil veriyoruz
  # Isim: Istanbul hatirasi
  # Yazar: Ahmet Umit
  # Sayfa sayisi: 561
  # Turu: Polisiye

print(len(kitap)) #561