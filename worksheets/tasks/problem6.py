# Problem 6
# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

# Hipotenüs Formülü: a^2 + b^2 = c^2

print('Dik ucgenin dik 2 kenarini gireceksiniz ve hipotenusunu hesaplayacagim')

x = int(input('Ilk kenar : '))
y = int(input('Ikinci kenar : '))
hipotenus = (x**2 + y**2) ** 0.5
print('Hipotenus = ', hipotenus)


