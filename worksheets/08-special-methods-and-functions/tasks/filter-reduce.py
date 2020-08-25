"""
  QUESTION:
  Elinizde şöyle bir liste bulunsun.
  [1,2,3,4,5,6,7,8,9,10]

  Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

  Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.
"""

list1 = [1,2,3,4,5,6,7,8,9,10]

newFilter1 = filter(lambda x: x % 2 == 0, list1)
newList1 = list(newFilter1)

from functools import reduce
listToplam = reduce(lambda x,y: x+y, list1)
ciftToplam = reduce(lambda x,y: x+y, newList1)
print(listToplam) #55
print(ciftToplam) #30