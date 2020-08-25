
#!ENUMERATE

#*LONG WAY
list1 = ['Elma', 'Armut', 'Muz', 'Kiraz']
i = 0
sonuc = list()
while i < len(list1):
  sonuc.append((i, list1[i]))
  i+=1
print(sonuc) #[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

#*WITH ENUMERATE
list1 = ['Elma', 'Armut', 'Muz', 'Kiraz']
newEnumerate1 = enumerate(list1)
newList1= list(newEnumerate1)
print(newEnumerate1) #<enumerate object at 0x000001D42652B700>
print(newList1) #[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

for i,j in enumerate(list1):
  print(i,j)
# 0 Elma
# 1 Armut
# 2 Muz
# 3 Kiraz

#*CIFT INDEX LILERI YAZDIRMAK
list1 = ['Elma', 'Armut', 'Muz', 'Kiraz']
for i,j in enumerate(list1):
  if i % 2 == 0:
    print(i,j)
# 0 Elma
# 2 Muz