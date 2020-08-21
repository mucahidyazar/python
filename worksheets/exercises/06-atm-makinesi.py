print("""
  ***********************************************
  Welcome to ATM Bank
  ************************************************

  1 Bakiye Sorgulama
  2 Para Yatirmak
  3 Para Cekmek

  Uygulamamizdan cikmak icin Q'ya basiniz
""")

bakiye = 1000

while True:
  islem = input('Islemi seciniz : ')
  if islem == 'q':
    print('Tekrar bekleriz')
    break
  elif islem == '1':
    print("Bakiyeniz {} TL'dir".format(bakiye))
  elif islem == '2':
    miktar = int(input('Yatirmak istediginiz miktar : '))
    bakiye += miktar
    print('Yatirilan tutar : {}\nTotal: {}'.format(miktar, bakiye))
  elif islem == '3':
    miktar = int(input('Cekmek istediginiz miktar : '))
    if bakiye - miktar < 0:
      print('Bu tutari cekemezsiniz')
      continue
    bakiye -= miktar
    print('Cekilen tutar : {}\nTotal: {}'.format(miktar, bakiye))
  else:
    print('Gecersiz islem')