
#!generatorslar iterable objeler olusturmak icin kullanilan objelerdir. (Ornek olarak fonksiyonlar gibi)
def kareleriAl():
  sonuc = []

  for i in range(1,6):
    sonuc.append(i**2)
  
  return sonuc

print(kareleriAl()) #[1, 4, 9, 16, 25]
#1000000 tane sayiyi bu sekilde bellekte saklamak mantikli olmayacakdir 
#bu yuzden generatorlari kullanabiliriz

def kareleriAl():
  for i in range(1,6):
    #Bu yield aslinda burada hicbirsey uretmiyor
    #Sadece uretmek icin hazir bekliyor
    #iterator olusturup next yaptigimiz zaman uretmeye basliyor
    yield i ** 2

generator = kareleriAl()
print(generator) #<generator object kareleriAl at 0x0000029664159AC0>

#Generator objemizden bir tane iterator obje olusturuyoruz
iterator = iter(generator)
#next iterator diyerek yield'in uretime baslamasini soyleriz ve ilk anahtarimiz 1 e erisiriz
print(next(iterator)) #1
print(next(iterator)) #4
print(next(iterator)) #9
print(next(iterator)) #16
print(next(iterator)) #25
#print(next(iterator)) #StopIteration

#Yeni generator tanimlasakda daha once generator tanimlanmissa 
#ve yield sona gelmisse yine hata aliriz
iterator2 = iter(generator)
#print(next(iterator2)) #StopIteration

#! List-comprehension to generation
liste = [i*3 for i in range(5)]
print(liste) #[0,3,6,9,12]
generator = (i*3 for i in range(5))
iterator = iter(generator)
print(next(iterator)) #0
print(next(iterator)) #3
print(next(iterator)) #6
print(next(iterator)) #9
print(next(iterator)) #12
#print(next(iterator)) #StopIteration

#!EXERCISE - CARPIM TABLOSU
def carpimTablosu():
  for i in range(1,3):
    for j in range(1,3):
      yield('{} x {} = {}'.format(i,j,i*j))
for i in carpimTablosu():
  print(i)
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

