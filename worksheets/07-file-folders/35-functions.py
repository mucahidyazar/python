
#! WITH OPEN
#dosyalar bu metoddan sonra otomatik olarak kapatilacagini biliriz yani burada file.close() yapmamiza gerek yoktur
with open('bilgiler.txt', 'r', encoding='utf-8') as file:
  for x in file:
    print(x, end="")
# Mustafa Murat Coskun
# Mucahid Yazar

#!SEEK
#Dosya okuma islemlerinde dosya imlecimiz okumaya gore yeri git gide en sona yaklasiyordu
#Seek ile bu imleci istedigimiz yere goturup oradan okuma islemi yapabilecegiz
#!TELL
#Dosya imlecinin nerede oldugunuda tell ile ogreniriz
#!DOSYALARI ILERI SARMAK VE OKUMAK
with open('bilgiler.txt', 'r', encoding='utf-8') as file:
  print(file.tell()) #0 Hic okuma yapmadik cunku
  file.seek(15)
  print(file.tell()) #15. byte da yani harfde oldugunu goruruz
  icerik1 = file.read(10) #15. byte dan 10byte sonraya kadar okuma yapar 
  # oskun
  # Muca
  print(icerik1)


















