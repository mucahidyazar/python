"""
  QUESTION:
  Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
  [(3,4),(10,3),(5,6),(1,9)]

  Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
  [12, 30, 30, 9]

  Not : map() fonksiyonunu kullanmaya çalışın.
"""

list1 = [(3,4),(10,3),(5,6),(1,9)]

newMap = map(lambda x : x[0]*x[1], list1)
newList = list(newMap)
print(newList)