
#! ALL
#Butun degerler True ise TRUE doner, en az bir deger False ise FALSE doner
list1 = [True, True, True, True, True]
list2 = [True, True, False, True, True]
list3 = [1,2,3,4,5,6]
def allLongWay(list):
  for i in list:
    if not i:
      return False
  return True
print(allLongWay(list1)) #True
print(allLongWay(list3)) #True
print(allLongWay(list2)) #False

#*WITH ALL
print(all(list1)) #True
print(all(list3)) #True
print(all(list2)) #False




#!ANY
#Herhangi bir deger True ise TRUE, hicbir deger True degilse veya hepsi False ise FALSE doner
list1 = [True, True, True, True, True]
list2 = [True, True, False, True, True]
list3 = [1,2,3,4,5,6]
list4 = [0,1,2,3,4,5,6]
def anyLongWay(list):
  for i in list:
    if i:
      return True
  return False

print(anyLongWay(list1)) #True
print(anyLongWay(list3)) #True
print(anyLongWay(list2)) #True
print(anyLongWay(list4)) #False

#*WITH ANY
print(any(list1)) #True
print(any(list3)) #True
print(any(list2)) #True
print(any(list4)) #False

