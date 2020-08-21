x = 10
y = 5
y = 9.5
z = 3
print(x-y) #0.5
print(x*x) #100
print(x+y+z) #22.5

"""
#DEGISKEN ISMI :
sayi ile baslayamaz
aralarinda bosluk olamaz
sembol olarak sadece _ kullanilabilir
pythondaki while gibi isimlendirmelerle degisken ismi olusturulamaz
"""
pi_sayisi = 3.14
cap = 4
cevre = pi_sayisi * cap
print('Cevre', cevre)

# Iki degiskeni birbiriyle degistirmek
a = 10
b = 4
a,b = b,a
print(a) #4
print(b) #10

# Iki farkli yontem
c = 5
c = c + 1
print(c) #6
d = 5
d += 1
print(d) #6