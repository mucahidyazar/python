# Problem 21 #Functions
print("""
  ***********************************************
  Mukemmel sayi bulma

  Nedir?
  1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
  hipotenusu bulmak icin

  Press Q to quit
  ************************************************
""")


def calcHipotenus(sayi1, sayi2):
  hipotenus = (sayi1**2 + sayi2**2) ** 0.5
  return hipotenus == int(hipotenus)

pisagorNumbers = []
for x in range(1,101):
  for y in range(1,101):
    if(calcHipotenus(x,y)):
      pisagorNumbers.append([x,y,(x**2 + y**2) ** 0.5])
print(pisagorNumbers)