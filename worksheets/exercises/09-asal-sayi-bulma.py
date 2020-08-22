#FUNCTION
print("""
  ***********************************************
  Asal Sayi Bulmak
  ***********************************************

  Nedir?
  1 ve kendisinden baska sayilara tam bolunmeyen sayilardir
  2,3,5,7,11... gibi
  
  Uygulamamizdan cikmak icin Q'ya basiniz
""")

def isAsal(sayi):
  if(sayi == 1):
    return False
  elif (sayi == 2):
    return True
  else:
    for i in range(2, sayi):
      if(sayi % i == 0):
        return False
    return True

while True:
  sayi = input('Sayi:')
  if (sayi == 'q'):
    break
  else:
    sayi = int(sayi)
    if (isAsal(sayi)):
      print(sayi,'asal bir sayidir')
    else:
      print(sayi,'asal bir sayi degildir')