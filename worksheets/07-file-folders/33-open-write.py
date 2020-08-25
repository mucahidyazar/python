
#!open(dosyaAdi, dosyaErismeKipi)

#!w dosya kipi
#Olusturmak istedigimiz dizinda o dosya yoksa olusturur, 
#*varsa silip yeniden olusturur

#!DOSYA KAPATMAK
#Asagidaki kodu calistirmak istedigimizde bu dosya ile ayni klasor altinda olusturur
#file = open('bilgiler.txt', 'w')
#Dosyalarimizi olusturduktan sonr sistemde yer harcamamasi icin kapatmamiz gerekiyor
#file.close()

#!DOSYA KAPATMAK
#baska dizinde ornegin desktopda
# file = open('C:/Users/Mucahid Yazar/OneDrive/Desktop/bilgiler.txt', 'w')
# file.close()

#!txt dosuyalarinda her bir harf 1 byte dir

#! W(WRITE) KIPI - DOSYA YAZMAK
#Turkce karakter kullanacagimiz zaman encodinge utf-8 kullanmak zorundayiz
file = open('bilgiler.txt', 'w', encoding="utf-8")
file.write('Mustafa Murat Coskun\n')
file.close()

#! A(APPEND) KIPI - DOSYAYA YAZI EKLEME
#\n buradada dosya icerisinde alt satira gecmemize yarar
file = open('bilgiler.txt', 'a', encoding="utf-8")
file.write('Mucahid Yazar\n')
file.close()