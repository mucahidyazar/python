# Problem 14
# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
# İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

print("""
  ***********************************************
  Toplama

  Press Q to quit
  ************************************************
""")

total = 0
while True:
  number = input('Please write a number : ')
  if(number == 'q'):
    print('Total = {}'.format(total))
    break
  total+=int(number)
