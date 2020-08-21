x = 'new string 1'
y = "new string 2"
z = """new string 3"""
print(z) #new string 3
a = "Murat's car"
print(a) #Murat's car
b = 'Murat\'s car'
print(b) #Murat's car
print(b[1]) #u
print(b[0]) #M
print(b[8]) #c
#- index ile tersten stringi alir
print(b[-1]) #r
print(b[-2]) #a
print(b[-3]) #c

c = 'Python Programlama Dili'
#string parcalama [baslama indexi:bitis indexi:atlama degeri]
#!!!bitis indexi dahil degildir
print(c[4:10]) #on Pro

#!!!solunda deger yoksa orasi bos birakilmis olarak dusunulur
#baslangic indexi vermezsek bastan baslar
print(c[:10]) #Python Pro
#bitis indexi vermezsek sona kadar devam eder
print(c[4:]) #on Programlama Dili
#son daki karakteri almamak
print(c[4:-1]) #on Programlama Dil
print(c[4:-3]) #on Programlama D
#Atlama degeri => Asagida harfleri 2 2 atlayarak alacak
print(c[::2]) #Pto rgalm ii
#4. indexden basla - 12. indexe kadar git - 2, 2 atlayarak topla
print(c[4:12:2]) #o rg
#Stringi tersten yazdirmak - -1 -1 atlayacagi icin terse dogru atlaya atlaya alir
print(c[::-1]) #iliD amalmargorP nohtyP

###!!! STRING OZELLIKLERI
d = 'Merhaba'
#Length bulmak
print(len(d)) #7

e = 'Hello'
f = 'world!'
print(e + ' ' + f) #Hello world!
print(e * 2) #HelloHello

#!!! Python'da stringler degistirilemez
# YANLIS => e[0] = P
# DOGRU => e = 'Pello'