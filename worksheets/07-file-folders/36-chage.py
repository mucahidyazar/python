
#! r+ KIPI - HEM DOSYA OKUMAK HEMDE YAZMAK 
with open('change-1.txt', 'r+', encoding='utf-8') as file:
  print(file.read())
#Mustafa Murat Coskun
with open('change-1.txt', 'r+', encoding='utf-8') as file:
  file.seek(10)
  file.write('Deneme')
with open('change-1.txt', 'r+', encoding='utf-8') as file:
  print(file.read())
#Mustafa MuDenemerat Coskun

with open('change-2.txt', 'a', encoding='utf-8') as file:
  file.write('Mert Eraslan\n')
  file.write('Semih Aktas\n')
with open('change-2.txt', 'r+', encoding='utf-8') as file:
  print(file.read())
# Mustafa Murat Coskun
# Mert Eraslan
# Semih Aktas

#!DOSYA BASINDA DEGISIKLIK
with open('change-2.txt', 'r+', encoding='utf-8') as file:
  icerik = file.read()
  icerik = 'Mehmet Keper\n' + icerik
with open('change-2.txt', 'r+', encoding='utf-8') as file:
  print(file.read())
# Mehmet Keper
# Mustafa Murat Coskun
# Mert Eraslan
# Semih Aktas

#!DOSYA SONUNDA DEGISIKLIK
with open('change-2.txt', 'r+', encoding='utf-8') as file:
  icerik = file.read()
  icerik = icerik + 'Mehmet Keper\n'
with open('change-2.txt', 'r+', encoding='utf-8') as file:
  print(file.read())
# Mustafa Murat Coskun
# Mert Eraslan
# Semih Aktas
# Mehmet Keper

#!DOSYA ORTASINDA DEGISIKLIK
#readlines ile array olarak dosya icerisindeki elemanlari alip inser ile bu arraye ekleyerek dosyalarin ortalarinda yapmak istedigimiz degisiklikleri yapabiliriz
with open('change-2.txt', 'r+', encoding='utf-8') as file:
  icerik = file.readlines()
  icerik.insert(2,'Asli Aydin\n') #Mert Eraslanin altina yani listenin 2. indexine
  file.seek(0)
  # for x in icerik:
  #   file.write(x)
  #OR
  file.writelines(icerik)

with open('change-2.txt', 'r+', encoding='utf-8') as file:
  print(file.read())
# Mustafa Murat Coskun
# Mert Eraslan
# Asli Aydin
# Semih Aktas
# Mehmet Keper