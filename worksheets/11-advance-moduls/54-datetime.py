
#!DATETIME
#Zaman ve tarih islemleri icin kullaniriz

from datetime import datetime

#Guncel konumumuzu turkiye olarak ayarlar ve asagidaki bilgileri Turkce aliriz
import locale
locale.setlocale(locale.LC_ALL, "")

#Suanin tarihini aliriz
print(datetime.now()) #2020-08-26 22:33:46.427900
print(datetime.now()) #2020-08-26 22:34:00.316438

suan = datetime.now()

print(suan.year) #2020
print(suan.month) #8
print(suan.day) #26
print(suan.hour) #22
print(suan.microsecond) #113243

#Guzel sekilde tarihi gostermek
print(datetime.ctime(suan)) #Wed Aug 26 22:36:21 2020

#!strftime
#Yil bilgisini almak : %Y
#Ay ismini almak %B
#Gun ismini almak %A
#Gun bilgisini almak %D
#Saat bilgisini almak %X
print(datetime.strftime(suan, '%Y')) #2020
print(datetime.strftime(suan, '%B')) #August
print(datetime.strftime(suan, '%A')) #Wednesday
print(datetime.strftime(suan, '%D')) #08/26/20
print(datetime.strftime(suan, '%X')) #22:39:12
print(datetime.strftime(suan, '%B %Y')) #August 2020

#!timestamp
#suanki tarihten timestampi aliriz
suan = datetime.now()
saniye = datetime.timestamp(suan)
print(saniye) #1598471074.598766

#!fromtimestamp
#timestampden suanki tarihi aliriz
suan2 = datetime.fromtimestamp(saniye)
print(suan2) #2020-08-26 22:44:34.598766

#1970 bir milattir timestamp icin
suan3 = datetime.fromtimestamp(0)
print(suan3) #1970-01-01 03:00:00

#!Kendi tarihimizi olusturmak
tarih1 = datetime(2019,12,1)
tarih2 = datetime(2021,12,1)
suan = datetime.now()
#!Belli iki tarih arasindaki farki bulmak
print(tarih1-suan) #-270 days, 1:10:50.657248
print(tarih2-suan) #461 days, 1:10:20.314176






