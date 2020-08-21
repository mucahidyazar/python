# Problem 8
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x > y and x > z:
  print('En buyuk sayi x ve degeri:', x)
elif y > x and y > z:
  print('En buyuk sayi y ve degeri:', y)
elif z > x and z > y:
  print('En buyuk sayi z ve degeri:', z)