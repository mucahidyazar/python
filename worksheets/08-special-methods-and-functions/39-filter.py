
#!FILTER
#Reduce fonksiyonuna cok benzer ama filter a gonderdigimiz fonksiyon bize mutlaka bir Boolean yani True yada False deger dondermelidir

#*CIFT SAYILARI ALMAK
#Fonksiyondan True donen degerler Filter Objesiyle bize donuyor
newFilter1 = filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8])
newList1 = list(newFilter1)
print(newFilter1) #<filter object at 0x00000116DB015790>
print(newList1) #[2, 4, 6, 8]

#*ASAL SAYI BULMAK
def isAsal(x):
  i = 2
  if x == 1:
    return False
  elif x == 2:
    return True
  else:
    while i < x:
      if x % i == 0:
        return False
      i +=1
    return True

newFilter2 = filter(isAsal, range(1,100))
newList2 = list(newFilter2)
print(newList2)
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


