
#!BREAK
#Loop breaki gordugu anda durur
i = 0
while i < 5:
  if i == 4:
    break
  print(i)
  i+=1
# 0
# 1
# 2
# 3

liste1 = [1,2,3,4]
for x in liste1:
  if x == 3:
    break
  print(x)
# 1
# 2

while True:
  isim = input('Isminizi girin(Cikmak icin Q ya basin)')
  if isim == 'q':
    break
  print('Isminiz : ', isim)

#!CONTINUE
#Az kullanilir ama ise yarar durumlarda kullaniliyor
#continue ile karsilasildiginda dongu loopun basina donuyor ve loopa kaldigi yerden devam ediyor
liste1 = [1,2,3,4,5,6]
for x in liste1:
  if x == 3 or x == 5:
    continue
  print(x)
# 1
# 2
# 4
# 6
