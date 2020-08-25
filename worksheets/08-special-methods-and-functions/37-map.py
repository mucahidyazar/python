
#! MAP
#map fonksiyonunda ilk argument olarak bir fonksiyon yazariz ve ikinci argument olarakda bir liste yazariz.
#map fonksiyonu bu listenin her elemanini bu fonksiyonuna gondererek yeni bir map objesi olusturur
#daha sonra biz bu map objesini listeye ceviririz asagidaki gibi
def double(x):
  return x * 2

newMap = map(double, [1,2,3,4,5]) #Burasi bize asagidaki gibi map objesi doner
print(newMap) #<map object at 0x0000021CBF887220>

#*Map objesini listeye tekrar cevirmek
newList = list(newMap)
print(newList) #[2, 4, 6, 8, 10]

newMap1 = map(lambda x : x ** 2, (1,2,3,4,5,6,7,8,9,10))
newList1 = list(newMap1)
print(newList1) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12,13]
newMap2 = map(lambda x,y : x*y, list1,list2)
#MANTIGI
# x = 1, x = 5
# x = 2, x = 6
# x = 3, x = 7
# x = 4, x = 8
newList2 = list(newMap2)
print(newList2) #[5, 12, 21, 32]

#3 TANE FONKSIYONDA GONDEREBILIRIZ
#list3de fazladan bir eleman(13) digerlerinde olmadigi icin YOK SAYILIR
newMap2 = map(lambda x,y,z : x*y*z, list1,list2,list3)
#MANTIGI
# x = 1, x = 5, z = 9
# x = 2, x = 6, z = 10
# x = 3, x = 7, z = 11
# x = 4, x = 8, z = 12
newList2 = list(newMap2)
print(newList2) #[45, 120, 231, 384]