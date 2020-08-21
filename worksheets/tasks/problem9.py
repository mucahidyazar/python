# Problem 9
# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
# Vize1 toplam notun %30'una etki edecek.
# Vize2 toplam notun %30'una etki edecek.
# Final toplam notun %40'ına etki edecek..

vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final = float(input('Final: '))

point = vize1 / 100 * 30 + vize2 / 100 * 30 + final / 100 * 40

if point >= 90:
  print('Notunuz: AA')
elif point >= 85:
  print('Notunuz: BA')
elif point >= 80:
  print('Notunuz: BB')
elif point >= 75:
  print('Notunuz: CB')
elif point >= 70:
  print('Notunuz: CC')
elif point >= 65:
  print('Notunuz: DC')
elif point >= 60:
  print('Notunuz: DD')
elif point >= 55:
  print('Notunuz: FD')
elif point < 55:
  print('Notunuz: FF')