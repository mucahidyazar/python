liste = ['Elma', 35, 'Merhaba', 3.14, 5]
print(type(liste)) #<class 'list'>

emptyList1 = []
print(emptyList1) #[]
emptyList2 = list()
print(emptyList2) #[]

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(newList)) #9

#!stringi listeye cevirmek
newList1 = list('Merhaba')
print(newList1) #['M', 'e', 'r', 'h', 'a', 'b', 'a']

#
newList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(newList2[0]) #1
print(newList2[3]) #4

#sondaki elemana erismek
print(newList2[-1]) #9
print(newList2[-2]) #8
print(newList2[-3]) #7

#listeleri parcalamak
print(newList2[4:]) #[5, 6, 7, 8, 9]
print(newList2[:5]) #[1, 2, 3, 4, 5]

#listeleri ters cevirmek
print(newList2[::-1])



#!Temel liste metodlari
newList3 = [1,2,3]
newList4 = [4,5,6]
newList5 = newList3 + newList4
print(newList5) #[1, 2, 3, 4, 5, 6]

#direk olarak degistirilebilirler
newList5[0] = 0
print(newList5) #[0, 2, 3, 4, 5, 6]

#ilk 2 elemani degistirmek
newList6 = [1, 2, 3, 4, 5, 6]
newList6[:2] = 10, 11
print(newList6) #[10, 11, 3, 4, 5, 6]



#!Liste metodlari
newList7 = [1, 2, 3, 4, 5, 6]
#append => listeye eleman ekleme
newList7.append(7)
print(newList7) #[1, 2, 3, 4, 5, 7]
#pop => listenin en son elemanini cikartir atar
newList7.pop()
print(newList7) #[1, 2, 3, 4, 5]
#pop ile index vererek atmak
newList7.pop(0)
print(newList7) #[2, 3, 4, 5]
#sort siralamak
newList8 = [11, 52, 13, 24, 65, 96]
newList8.sort()
print(newList8) #[11, 13, 24, 52, 65, 96]
#trersten siralamak
newList8.sort(reverse = True)
print(newList8) #[96, 65, 52, 24, 13, 11]

newList9 = [1, 2, 3, 4, 5, 6]
print(newList9[50]) #Error

newList9 = [[1, 2], [3, 4], [5, 6]]
print(newList9[0][1]) #2












