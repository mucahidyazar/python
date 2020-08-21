# Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
# Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
# Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
# Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

print("""
  ***********************************************
  Ucgen ve Dortgen Analyze


  # Shapes

  1 Ucgen
  2 Dortgen
  ************************************************
""")

shape = input('Ucgen mi yoksa Dortgen mi?')

if shape == '1':
  first = int(input('Ilk kenar uzunlugu?'))
  second = int(input('Ikinci kenar uzunlugu?'))
  third = int(input('Ucuncu kenar uzunlugu?'))

  if first == second and first == third:
    print('Bu bir eskenar ucgen')
  elif first == second or first == third or second == third:
    print('Bu bir eskenar ucgen')
  elif first <= 0 or second <= 0 or third <= 0:
    print('Bu inputlar gecersiz bir sekil olusturuyor')
  else:
    print('Bu bir siradan ucgen')
elif shape == '2':
  first = int(input('Ilk kenar uzunlugu?'))
  second = int(input('Ikinci kenar uzunlugu?'))
  third = int(input('Ucuncu kenar uzunlugu?'))
  fourth = int(input('Dorduncu kenar uzunlugu?'))

  if first == second and first == third and first == fourth:
    print('Bu bir kare')
  elif first == third and second == fourth and first != fourth:
    print('Bu bir dikdortgen')
  elif first <= 0 or second <= 0 or third <= 0 or fourth <= 0:
    print('Bu inputlar gecersiz bir sekil olusturuyor')
  else:
    print('Bu bir siradan dortgen')
else:
  print('Lutfen shape icin gecerli bir input verisi giriniz. Ornegin: 1')




