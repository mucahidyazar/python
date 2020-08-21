
liste1 = [1,2,3,4,5]
liste2 = list()

for i in liste1:
  liste2.append(i)

print(liste2) #[1, 2, 3, 4, 5]

#!LIST COMPREHENSION
liste3 = [1,2,3,4,5,6]
#for i in liste3 => burada i liste icinde gezecek ve ilk bastaki i 'ye yani liste4 e eklenecek
#ilk bastaki i for icindeki listeyi dolasan dongu degeriyle ayni olmali yoksa listeye ekleme isini yapamaz.
liste4  = [i for i in liste3]
print(liste4) #[1, 2, 3, 4, 5, 6]

liste5 = [1,2,3,4,5,6]
liste6  = [i*2 for i in liste5]
print(liste6) #[2, 4, 6, 8, 10, 12]

liste7 = [(1,2), (3,4), (5,6)]
liste8 = [i*j for i,j in liste7]
print(liste8) #[2, 12, 30]

string1 = 'Python'
liste9 = [i*3 for i in string1]
print(liste9) #['PPP', 'yyy', 'ttt', 'hhh', 'ooo', 'nnn']

liste10 = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste11 = []
for i in liste10:
  for x in i:
    liste11.append(x)
print(liste11) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
liste12 = [x for i in liste10 for x in i]
print(liste12) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]