# Problem 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

mukemmel = False
sayi = int(input('Sayi giriniz ve mukemmel sayi mi ogreniniz : '))
toplam = 0

if sayi < 1:
  print('Gecersiz bir sayi girdiniz')
for i in range(sayi):
  if i == 0:
    continue
  if sayi % i == 0:
    toplam+=i

print(toplam)
if sayi > 0 and toplam == sayi:
  print('Mukemmel sayi', sayi)
elif sayi > 0:
  print('Normal sayi')