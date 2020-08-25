#ERRORS
print("""
  ***********************************************
  Catching Errors
  ***********************************************

  Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, 
  eğer sayı çift ise return ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon 
  raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar 
  bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece 
  çift sayıları bastırın.
""")

liste = [11,22,35,26,36,68,9]

def ciftmi(sayi):
  if sayi % 2 == 0:
    return sayi
  else:
    raise ValueError('Bu sayi CIFT bir sayi degildir.')

for x in liste:
  try:
    print(ciftmi(x))
  except ValueError:
    pass