
#!ZIP
#Bu fonksiyonla asagidaki 2 demeti 3. demete cevirme gibi isleri yapiyoruz
#list1=[1,2]
#list2=[3,4]
#list3=[(1,3),(2,4)]

#LONG WAY
list1=[1,2]
list2=[3,4]
i = 0
list3=list()
while ( i < len(list1) and i < len(list2)):
  list3.append((list1[i], list2[i]))
  i+=1
print(list3) #[(1, 3), (2, 4)]

#*SHORT WAY
newZip1 = zip(list1, list2)
newList1 = list(newZip1)
print(newZip1) #<zip object at 0x00000217C178B600>
print(newList1) #[(1, 3), (2, 4)]


#*ZIP FONKSIYONUYLA @ LISTE UZERINDE GEZINMEK **********
list1=[1,2]
list2=['Python', 'Javascript']
for i,j in zip(list1, list2):
  print(i,j)
# 1 Python
# 2 Javascript

#*ZIP with DICTIONARIES
dict1 = { 'Elma': 1, 'Armut': 2, 'Kiraz': 3 }
dict2 = { 'Sifir': 0, 'Bir': 1, 'Iki': 2 }
newZip2 = zip(dict1, dict2)
newList2 = list(newZip2)
print(newList2) #[('Elma', 'Sifir'), ('Armut', 'Bir'), ('Kiraz', 'Iki')]
#*WITH VALUES
newZip3 = zip(dict1.values(), dict2.values())
newList3 = list(newZip3)
print(newList3) #[(1, 0), (2, 1), (3, 2)]


