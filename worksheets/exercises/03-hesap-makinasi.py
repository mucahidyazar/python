print("""
  ***********************************************
  Hesap Makinasi Programi


  # Islemler

  1. Toplama Islemi
  2. Cikarma Islemi
  3. Carpma Islemi
  4. Bolme Islemi
  ************************************************
""")

a = int(input('Birinci sayi: '))
b = int(input('Ikinci sayi: '))

islem = input('Islem: ')

if islem == '1':
  print("{} ile {}'in toplami {}'dir".format(a, b, a+b))
elif islem == '2':
  print("{} ile {}'in farki {}'dir".format(a, b, a-b))
elif islem == '3':
  print("{} ile {}'in carpimi {}'dir".format(a, b, a*b))
elif islem == '4':
  print("{} ile {}'in bolumu {}'dir".format(a, b, a/b))
else:
  print('Gecersiz islem!')