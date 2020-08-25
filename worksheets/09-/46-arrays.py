
#!APPEND
#Liste sonuna eleman ekler
liste1 = [1,2,3,4,5,6]
liste1.append(7)
print(liste1) #[1,2,3,4,5,6,7]

#!EXTEND
#Bir listenin butun elemanlarini diger listeye ekler
liste1 = [1,2,3,4,5,6]
liste2 = [10,20,30]
liste1.extend(liste2)
print(liste1) #[1,2,3,4,5,6,10,20,30]

#!INSERT(index, x)
#Listenin herhangi bir indexine eleman ekleyebiliriz
liste1 = [1,2,3,4,5,6]
liste1.insert(2, 'Python') #2. indexe Python'u ekler
print(liste1) #[1,2,'Python',3,4,5,6]

#!POP
#Listenin sonundan eleman cikartmak
liste1 = [1,2,3,4,5,6]
liste1.pop()
print(liste1) #[1,2,3,4,5]
liste1.pop(2) #belirlenen indexdeki elemani cikartir
print(liste1) #[1,2,4,5]

#!REMOVE
#Elemanin kendisini yazarak listeden cikarma islemi yapariz
liste1 = ['Python', 'Java', 'Javascript']
liste1.remove('Python')
liste1.remove('C#') #Error
print(liste1) #['Java', 'Javascript']

#!INDEX
#Yoksa hata doner varsa buldugu ilk karakterin indexini doner
liste1 = [1,2,3,4,5,6]
liste2 = [1,2,2,3,3,6]
print(liste1.index(3)) #2
print(liste2.index(3)) #3
print(liste2.index(999)) #ValueError #*Eger yoksa
#3 degerini ara 4. indexden aramaya baslada diyebiliriz
print(liste2.index(3, 4)) #4

#!COUNT
#Verilen degerin lsitede kac defa gectigini bulur
liste2 = [1,2,2,3,3,6]
print(liste2.count(2)) #2
print(liste2.count(3)) #2
print(liste2.count(99)) #0

#!SORT
#Bir listenin elemanlarini sayiysa kucukten buyuge
#harfse alfabetik olarak siralama yapar
#reverse=True dersekte buyukten kucuge siralama yapar
liste = [1,3,2,55,32,16,99,5,22,226]
liste.sort()
print(liste) #[1, 2, 3, 5, 16, 22, 32, 55, 99, 226]
liste.sort(reverse=True)
print(liste) #[226, 99, 55, 32, 22, 16, 5, 3, 2, 1]
