import sqlite3

#Veritabanina baglanmak
con = sqlite3.connect('kutuphane.db')

#Veritabani uzerinde islem yapmak icin cursor bir degisken olusturmak
cursor = con.cursor()

def tabloOlustur():
  #execure = calsitir
  #!SQLITE3 TABLO OLUSTURMAK CREATE TABLE or CREATE TABLE IF NOT EXISTS
  #kitaplik => tablo adi
  cursor.execute('CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT, Yazar TEXT, Yayinevi TEXT, Sayfa_Sayisi INT)')
  #Yukaridaki veri tabanini commit etmek yani veri tabanina komut vermek
  con.commit()
tabloOlustur()

#!Basit veri ekleme => insert into
def veriEkle():
  cursor.execute("insert into kitaplik values('Istanbul Hatirasi', 'Ahmet Umit', 'Everest', 561)")
  con.commit()
#veriEkle()

#!Kullanicidan veri alarak
#Bu ? aslinda javascriptteki `` isaretinin icinde $ isareti kullanilmasi gibidir
#isim 1. soru isaretinin yerine gececek
#yazar 2. soru isaretinin yerine gececek
#yayinevi 3. soru isaretinin yerine gececek
#sayfaSayisi 4. soru isaretinin yerine gececek
def veriEkleDynamic(isim,yazar,yayinevi,sayfaSayisi):
  cursor.execute('insert into kitaplik values(?,?,?,?)',(isim,yazar,yayinevi,sayfaSayisi))
  con.commit()

# isim = input('Isim: ')
# yazar = input('Yazar: ')
# yayinevi = input('Yayinevi: ')
# sayfaSayisi = int(input('Sayfa sayisi: '))
# veriEkleDynamic(isim, yazar, yayinevi, sayfaSayisi)

#!Tablodaki verileri cekme
#*Select * From kitaplik #Tum kitaplari alir
#*Select Isim,Yazar From kitaplik #Tum kitaplarin isim ve yazarlarini alir
#*Select * From kitaplik where Yayinevi = 'Everest'

def verileriAl():
  cursor.execute('select * from kitaplik')
  liste = cursor.fetchall()
  #*print(liste) #[('Istanbul Hatirasi', 'Ahmet Umit', 'Everest', 561), ('Mucahid', 'Mucahid Yazar', 'Gokturk', 999)]
  print('Kitaplik tablosu bilgileri')
  for i in liste:
    print(i)
  #Burada con.commit yapmaya gerek yoktur cunku veritabanini degistirmiyoruz
#*verileriAl() 
# ('Istanbul Hatirasi', 'Ahmet Umit', 'Everest', 561)
# ('Mucahid', 'Mucahid Yazar', 'Gokturk', 999)

def verileriAl2():
  cursor.execute('select Isim,Yazar from kitaplik')
  liste = cursor.fetchall()
  for i in liste:
    print(i)
#*verileriAl2()
# ('Istanbul Hatirasi', 'Ahmet Umit')
# ('Mucahid', 'Mucahid Yazar')

def verileriAl3(yayinevi):
  cursor.execute('select * from kitaplik where Yayinevi = ?', (yayinevi,))
  liste = cursor.fetchall()
  for i in liste:
    print(i)
#*verileriAl3('Gokturk')
#('Mucahid', 'Mucahid Yazar', 'Gokturk', 999)
#*verileriAl3('Everest')
#('Istanbul Hatirasi', 'Ahmet Umit', 'Everest', 561)

#!VERILERI GUNCELLEMEK => UPDATE kitaplik set Yayinevi = 'Everest' where Yayinevi='Dogan Kitaplik'
#Yayin evi Dogan Kitaplik olan kitaplarin yain evini everest olarak gunceller
def verileriGuncelle(eskiYayinevi, yeniYayinEvi):
  cursor.execute('UPDATE kitaplik set Yayinevi = ? where Yayinevi = ?', (yeniYayinEvi, eskiYayinevi))
  con.commit()
#Gokturk yayinevine sahip kitaplarin yayinevlerini Everest yapar
#*verileriGuncelle('Gokturk', 'Everest')

#!VERILERI SILMEK => Delete From kitaplik where Yazar = 'Ahmet Umit'
def verileriSil(yazar):
  cursor.execute('DELETE From kitaplik where Yazar = ?', (yazar,))
  con.commit()
verileriSil('Mucahid Yazar')

#Isimiz bittikten sonra baglantiyi kapatmak
con.close()