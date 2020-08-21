# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

x = int(input('x : '))
y = int(input('y : '))

x,y = y,x
print('x : {}\ty: {}'.format(x, y))