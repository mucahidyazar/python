#MODULES
print("""
  ***********************************************
  Sayi Tahmin Oyunu
  ***********************************************

  1 ile 40 arasindaki sayiyi tahmin edin
  
  Uygulamamizdan cikmak icin Q'ya basiniz
""")

import random #Rastgele sayi uretmek icin
import time #Programimizin bir saniye bekletmek icin

rastgeleSayi = random.randint(1,40)
tahminHakki = 7

while True:
  tahmin = input('Tahmininiz :')
  if(tahmin == 'q'):
    break
  tahmin = int(tahmin)

  if(tahminHakki == 0):
    print('Tahmin hakkiniz bitti')
    print('Sayimiz:',rastgeleSayi)
    break
  if(tahmin < rastgeleSayi):
    print('Bilgiler sorgulaniyor...')
    time.sleep(1)
    print('Daha yuksek bir sayi soyleyin')
    tahminHakki -= 1
  elif(tahmin > rastgeleSayi):
    print('Bilgiler sorgulaniyor...')
    time.sleep(1)
    print('Daha dusuk bir sayi soyleyin')
    tahminHakki -= 1
  else:
    print('Bilgiler sorgulaniyor...')
    time.sleep(1)
    print('Tebrikler sayimiz :',tahmin)
    break




