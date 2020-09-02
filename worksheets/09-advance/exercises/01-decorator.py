
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