print("""
  QUESTION:
  Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

      isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
      soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
""")

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

newMap = map(lambda x,y: x+' '+y, isimler,soyisimler)
newArray = list(newMap)
newArray.sort()
print(newArray)

