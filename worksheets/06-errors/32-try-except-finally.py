
#!Javascriptteki try catch gibidir
#!try icine hata verebilecek kodlarimizi yaziyoruz

#a = int('asdasdasd213') #ValueError

#ozel bir except kosulu belirtmedigimiz icin try icinde olacak tum hatalar durumunda
#asagidaki except calisacaktir
try:
  a = int('asdasdasd213')
  print('Program burada')
except:
  print('Bir hata olsutu')
print('Blocklar sona erdi')
#Bir hata olustu
#Blocklar sona erdi

#!OZEL HATA YAKALAMA
try:
  a = int('asdasdasd213')
  print('Program burada')
except ValueError: #sadece ValueError lari yakalar
  print('Bir hata olsutu')
print('Blocklar sona erdi')

#!IKI TANE OZEL HATA
#Kullanici sayi yerine harf girerse except ValueError calisacak
#Herhangi bir inputa 0 girerse ZeroDivisionError calisacakdir
try:
  a = int(input('Bolunecek sayi : '))
  b = int(input('Bolen sayi : '))
  print('Sonuc: ', a/b)
except ValueError:
  print('Bir hata olsutu')
except ZeroDivisionError:
  print('Bu bolunen bu bolene bolunemez')

#!BIRDEN COK HATAYI AYNI EXCEPT ICINDE YAKALAMAK
try:
  a = int(input('Bolunecek sayi : '))
  b = int(input('Bolen sayi : '))
  print('Sonuc: ', a/b)
except (ValueError,ZeroDivisionError):
  print('Bir hata olsutu')

#!FINALLY
#Mutalaka calismasi gereken kodlari buraya yazariz
#Ne hata olursa olsun veya hata olmasa bile FINALLY block u calisacakdir
try:
  a = int(input('Bolunecek sayi : '))
  b = int(input('Bolen sayi : '))
  print('Sonuc: ', a/b)
except ValueError:
  print('Bir hata olsutu')
except ZeroDivisionError:
  print('Bu bolunen bu bolene bolunemez')
finally:
  print('Ne hata olursa olsun veya hata olmasa bile burasi calisacakdir')

#!HATA FIRLATMA
#raise hataAdi('Opsiyonel hata mesaji')
#Hata adi Pythonda tanimli hata adlarindan birisi olmalidir. Like ValueError, ZeroDivisionError
def tersCevir(s):
  if type(s) != 'str':
    raise ValueError('Lutfen string bir deger gonderin')
  else:
    return s[::-1]
print('Python') #nohtyP
print(12) #ValueError: Lutfen string bir deger gonderin