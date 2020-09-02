#for dongulerinde, list comprehensionlarinda ve generatorlerde karsimiza cikar
#Her seferinde bir tane eleman donen objedir
#Kendisinden iterable olusturabilecegimiz her obje bir iterable objedir
#*Tuple lar Listeler Stringler aslinda bir iterable objedir
#!Bir objenin iterable olabilmesi icin __iter__ ve __next__ metodlarini mutlaka tanimlanmali

#!ITERATOR OLUSTURMA
liste = [1,2,3,4,5]
#print(dir(liste)) #Metodlari goruruz

#artik liste uzerinde iterator objemiz olusmus olacak
iterator = iter(liste)

print(iterator) #<list_iterator object at 0x00000220713C5790>
print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #4
print(next(iterator)) #5
#Tum dizi elemanlarini gezdigimiz icin bir sonraki next te hata alacagiz
print(next(iterator)) #StopIteration

#!Ne ise yarar?
#for dongusunde biz gormesekde iterator kullanilir

#!Kendi Iterable Objelerimizi Olusturmak
#Olusturacagimiz siniflarda __iter__ __next__ metodlarini tanimlamaliyiz
class Kumanda():
  def __init__(self, kanalListesi):
    self.kanalListesi = kanalListesi
    self.index = -1
  
  def __iter__(self):
    #burada self diyere yukaridaki gibi sanki #iterator = iter(liste)# boyle yaspmis gibi oluyoruz
    #yani Kumandayi #iterator = iter(liste)# boyle ITERABLE yapiyoruz
    return self

  def __next__(self):
    self.index += 1
    if self.index < len(self.kanalListesi):
      return self.kanalListesi[self.index]
    else:
      self.index = -1
      raise StopIteration

kumanda = Kumanda(['Atv', 'Trt', 'Fox', 'KanalD', 'Ntv'])
iterator = iter(kumanda)
print(next(iterator)) #Atv
print(next(iterator)) #Trt
print(next(iterator)) #Fox

#! Iteratora cevirdigimiz objelerimizde arraylerdeki gibi loop donebiliriz
for i in kumanda:
  print(i)
# Atv
# Trt
# Fox
# KanalD
# Ntv


