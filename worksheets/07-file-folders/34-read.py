
#! R(READING) KIPI
#open ile acmaya calistigimiz dosya eger bulunmuyorsa 'FileNotFoundError' kipiyle error verir
try:
  file = open('bilgiler.txt', 'r')
  print(file)
  file.close()
except FileNotFoundError:
  print('Dosya bulunamadi!')

#for dongusuyle her bir satirini okuyabiliriz dosyalarimizin
#encoding turkce karakterleri okuyabilmek icin
try:
  file = open('bilgiler.txt', 'r', encoding='utf-8')
  for x in file:
    print(x, end = '') 
    #Her elemandan sonra Pythonun koydugu \n karakterini kaldirir
    #Dosyayi olustururken bizde \n koymustuk o yuzden her karakterden sonra 2 tane \n koyuluyor bunu istemedigimiz icin pythonun burada koydugu \n'i kaldiriyoruz end argumenti ile
  file.close()
except FileNotFoundError:
  print('Dosya bulunamadi!')
# Mustafa Murat Coskun
# Mucahid Yazar

#! READ FONKSIYONU
try:
  file = open('bilgiler.txt', 'r', encoding='utf-8')
  icerik = file.read()
  # Mustafa Murat Coskun
  # Mucahid Yazar
  icerik2 = file.read()
  print(icerik)
  print(icerik2) #Ilk basta okuyup dosyanin en sonuna gittigi icin burasi birsey yazmaz ekrana
except FileNotFoundError:
  print('Dosya bulunamadi!')

#! READLINE
#Herseferinde cagrildiginda bir satir okuyor. Yani bunu farkli farkl idegiskenlere atarak kullanabiliriz
try:
  file = open('bilgiler.txt', 'r', encoding='utf-8')
  icerik = file.readline()
  icerik2 = file.readline()
  print(icerik) # Mustafa Murat Coskun
  print(icerik2) # Mucahid Yazar
  #Tum satir bittiginde dosyanin yeni degiskenler bos donecektir
except FileNotFoundError:
  print('Dosya bulunamadi!')

  #! READLINES
#Herseferinde cagrildiginda bir satir okuyor. Yani bunu farkli farkl idegiskenlere atarak kullanabiliriz
try:
  file = open('bilgiler.txt', 'r', encoding='utf-8')
  icerik = file.readlines()
  print(icerik) #['Mustafa Murat Coskun\n', 'Mucahid Yazar\n']
  icerik2 = file.readlines()
  print(icerik2) # []
  #Tum satir bittiginde dosyanin yeni degiskenler bos donecektir
except FileNotFoundError:
  print('Dosya bulunamadi!')
