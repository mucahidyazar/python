a = True
b = False
print(type(a)) #<class 'bool'>
print(type(b)) #<class 'bool'>

#Pythonda bir sayi degeri 0 dan farkliysa True, 0'sa False'dir
print(bool(0)) #False
print(bool(1)) #True
print(bool(99)) #True
print(bool(-5)) #True

#Sayilarla Bool almak
print(1 == 1) #True
print(1 == 2) #False

#Hemen deger atamayacagimiz degiskenlere None atayabiliriz
c = None #Henuz deger atamasi yapilmamis
print(a) #None
c = 4
print(a) #4

#Karsilastirma operatorleri
# == (Esittir) => 2 deger birbirine esitse sonuc True degilse False doner
# != (Esit degildir) => 2 deger birbirine esit degilse True, esit ise False doner
# > (Buyuktur) => Soldaki degerin sagdaki degerden buyuk olup olmadigini denetler
# < (Buyuktur) => Sagdaki degerin soldaki degerden buyuk olup olmadigini denetler
# >= (Buyuk esittir)
# <= (Kucuk esittir)

print('Mehmet' == 'Mehmet') #True
print('Mehmet' == 'Murat') #False
print([1,2,3] == [1,2,3]) #True
print([1,2,3] == [1,2]) #False
print('Mehmet' != 'Murat') #True
print('Araba' < 'Murat') #True #Sozluk sirasina gore siralama yapar

