"""
  QUESTION:
  Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.
  [(3,4,5),(6,8,10),(3,10,7)]

  Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.
  [(3, 4, 5), (6, 8, 10)]
"""

list1 = [(3,4,5),(6,8,10),(3,10,7)]

def isPisagor(x):
  if x[0]**2 + x[1]**2 == x[2]**2:
    return True
  return False

newFilter = filter(isPisagor, list1)
newList = list(newFilter)
print(newList) #[(3, 4, 5), (6, 8, 10)]