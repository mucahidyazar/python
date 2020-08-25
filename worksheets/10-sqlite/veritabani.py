import sqlite3

#Veritabanina baglanmak
con = sqlite3.connect('kutuphane.db')

#Veritabani uzerinde islem yapmak icin cursor bir degisken olusturmak
cursor = con.cursor()

con.close()