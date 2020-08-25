#!Kume olusturmak
x = {1,2,3}
print(type(x)) #set
x2 = set()
print(type(x2)) #set

list1 = [1,2,3,3,1,1,2,2,2]
x3 = set(list1)
print(type(x3)) #set
print(x3) #{1, 2, 3}
#!Kumelerde her elemandan 1 tane olur


#!For dongusuyle gezilebilir
list2 = ['Elma', 'Armut', 'Kiraz', 'Muz']
for i in list2:
  print(i)
# Elma
# Armut
# Kiraz
# Muz

x4 = {'Python', 'Php', 'Java', 'Javascript'}
#print(x4[0]) #Error
#print(x4['python']) #Error
#!Ulasmak icin listeye cevirip ulasin
list3 = list(x4)
print(list3) #['Php', 'Java', 'Python', 'Javascript']


###
### !KUME METODLARI
###
#!ADD(x)
x5 = {1,2,3,4,5}
x.add(6)
print(x5) #{1,2,3,4,5,6}
x.add(4) #*Bu gibi ayni eleman ekleme islemlerinde birsey olmaz
print(x5) #{1,2,3,4,5,6}

#!DIFFERENCE(x)
#Farkl ielemanlari bulur
x6 = {1,2,3,4,5}
x7 = {1,2,32,54,5}
print(x6.difference(x7)) #{3, 4}
print(x7.difference(x6)) #{32, 54}

#!DIFFERENCE_UPDATE(x)
#Farklari bulup guncelleme islemlerini yapar
#Yani asagida x6 nin x7 den farkini bulup onu x6nin yeni kumesi yapar.
x6.difference_update(x7)
print(x6) #{3, 4}
print(x7)

#!DISCARD(x)
#Kumeden eleman cikarmak, cikarmak istedigimiz deger kumede yoksa hicbirsey yapmaz, hata bile vermez
x9 = {1,2,3,4,5}
x9.discard(2)
print(x9) #{1,3,4,5}
x9.discard(100)
print(x9) #{1,3,4,5}

#!INTERSECTION(x)
#Kume kesisimlerini bulur
x10 = {1,2,3,4,5}
x11 = {1,2,32,54,5}
print(x10.intersection(x11)) #{1,2,5}
#!INTERSECTION_UPDATE(x)
#Kesisim kumesini yakalar ve guncellemesini yapar
x12 = {1,2,3,4,5}
x13 = {1,2,32,54,5}
print(x12.intersection_update(x13)) #{1,2,5}

#!ISDISJOINT()
#Eger iki kumenin kesisim kumesi bos ise True, degilse False doner
x14 = {1,2,3,4,5}
x15 = {1,2,32,54,5}
x16 = {100}
print(x12.isdisjoint(x15)) #False #Ayrik kume degil der
print(x12.isdisjoint(x16)) #True #Ayrik kume der

#!ISSUBSET()
x17 = {1,2,3}
x18 = {1,2,3,4}
x19 = {5,6,7}
print(x17.issubset(x18)) #True
print(x17.issubset(x13)) #False

#!UNION(x)
#Her eleman 1 tane olacak sekilde tum kume elemanlarini birlestirir
x20 = {4,5,6,7}
x21 = {1,2,3,4}
print(x20.union(x21)) #{1, 2, 3, 4, 5, 6, 7}
#!UPDATE(x)
#Her elemanda bir tane olacak sekilde kumeleri birlestirir ve gunceller
print(x20.update(x21)) #{1, 2, 3, 4, 5, 6, 7}
































































































































