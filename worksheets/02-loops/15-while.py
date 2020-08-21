x = 0

while x < 5:
  print("x'nin degeri : ", x)
  x+=1
# x'nin degeri :  0
# x'nin degeri :  1
# x'nin degeri :  2
# x'nin degeri :  3
# x'nin degeri :  4

x = True
y = 0

while x == True:
  y+=1
  print(y)
  if y > 6:
    x=False
# 1
# 2
# 3
# 4
# 5
# 6
# 7

liste1 = [1,2,3,4,5]
index = 0
while index < len(liste1):
  print('index:', index, 'liste elemani:', liste1[index])
  index+=1
# index: 0 liste elemani: 1
# index: 1 liste elemani: 2
# index: 2 liste elemani: 3
# index: 3 liste elemani: 4
# index: 4 liste elemani: 5