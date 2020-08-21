# Problem 3
# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
# İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.

print("""
  ***********************************************
  Carpim Tablosu
  ************************************************
""")

for x in range(1,11):
  for y in range(1,11):
    print("{} x {} = {}".format(x,y,x*y))
#print(*range(1,11)) #1 2 3 4 5 6 7 8 9 10