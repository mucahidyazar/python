print("""
  ***********************************************
  Faktoriyel Bulmak
  ***********************************************

  Uygulamamizdan cikmak icin Q'ya basiniz
""")
#5! => 5.4.3.2.1
#7! => 7.6.5.4.3.2.1
#3! => 3.2.1

while True:
  sayi = input('Sayi : ')
  if sayi == 'q':
    print('Program sonlandiriliyor...')
    break
  else:
    sayi = int(sayi)
    faktoriyel = 1
    for i in range(2, sayi+1):
      faktoriyel *= i
    print(faktoriyel)