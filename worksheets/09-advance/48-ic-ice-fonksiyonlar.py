
#!FONKSIYONU DEGISKENE ATAYARAK KOPYALAMAK
def selamla(isim):
  print('Selam', isim)
selamla('Ayse') #Selam Ayse

merhaba = selamla
merhaba('Mucahid') #Selam Mucahid


#!IC ICE FONKSIYONLAR
def fonksiyon():
  def fonksiyon2():
    print('Kucuk fonksiyondan herkese merhaba')
  fonksiyon2()
  print('Buyuk fonksiyondan herkese merhaaba')
fonksiyon()

def fonksiyon(*args):
  def toplama(args):
    toplam = 0
    for i in args:
      toplam += i
    return toplam
  print(toplama(args))
fonksiyon(1,2,3,4,5,6,7) #28