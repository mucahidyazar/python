
#!OS
#Isletim sisteminde islemler gerceklestirebiliyoruz.

import os

#dir(os) => os modulundeki methodlari gorebiliriz

#!Bulundugumuz dizini almak
print(os.getcwd()) #C:\Users\Mucahid Yazar\OneDrive\Desktop\notes\python\worksheets\11-advance-moduls

#!Bulundugumuz dizini degistirmek
#*os.chdir('C:/Users/user/Desktop')
print(os.getcwd()) #C:/Users/user/Desktop

#!Suanki bulundugumuz dizindeki butun dosya ve klasorleri listeler
print(os.listdir()) #['54-datetime.py', '55-os.py']

#!Bulundugumuz dizinde klasor olusturmak
#varsa olusturmaz yoksa olusturur.
#*os.mkdir('deneme') #deneme adinda klasor olusturur

#!MAKEDIRS => Ic ice klasorler olusturabiliriz
#*os.makedirs('deneme2/deneme3')

#!RMDIR => KLASOR SILMEK
#*os.rmdir('deneme2/deneme3')

#!REMOVEDIRS => hem deneme2 hem deneme3 u siler
#*os.removedirs('deneme2/deneme3')

#!RENAME => Dosya ismi degistirmek
#*os.rename('dosya.txt', 'newdosya.txt')

from datetime import datetime
#!STAT => Dosya ozelliklerini almak
print(os.stat('newdosya.txt'))
print(os.stat('newdosya.txt').st_mtime) #1598472122.8199456
print(datetime.fromtimestamp(os.stat('newdosya.txt').st_mtime)) #2020-08-26 23:02:02.819946
#os.stat_result(st_mode=33206, st_ino=22236523161085170, st_dev=3156106114, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1598472122, st_mtime=1598472122, st_ctime=1598472122)

#!WALK
print(os.walk('C:/Users/Mucahid Yazar/OneDrive/Desktop')) #<generator object walk at 0x0000021B526412E0>
for i in os.walk('C:/Users/Mucahid Yazar/OneDrive/Desktop/psd-files'):
  print(i)
#Klasor Yolu-Icindeki Klasor Isimleri,Icindeki Dosya Isimleri
# (
#   'C:/Users/Mucahid Yazar/OneDrive/Desktop/psd-files', 
#   [], 
#   ['card.psd', 'check-0001.psd', 'check-0002.psd', 'down-0001.psd', 'down-0002.psd', 'icon-0010.psd', 'icon-0011.psd', 'icon-0012.psd', 'icon-0013.psd', 'icon-0014.psd', 'icon-0015.psd', 'left-0002.psd', 'no-image.psd', 'right-0001.psd', 'right-0002.psd', 'up-0002.psd']
# )



