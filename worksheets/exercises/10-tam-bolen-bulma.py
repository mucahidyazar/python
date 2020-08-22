#FUNCTION
print("""
  ***********************************************
  Tam Bolen Sayi Bulmak
  ***********************************************
  
  Uygulamamizdan cikmak icin Q'ya basiniz
""")

def tamBolenBul(sayi):
  tamBolenler = []
  for i in range(2,sayi):
    if(sayi % i == 0):
      tamBolenler.append(i)
  return tamBolenler

while True:
  sayi = input('Sayi:')
  if(sayi == 'q'):
    print('Program sonlandirildi')
    break
  else:
    sayi = int(sayi)
    print('Tam bolenler', tamBolenBul(sayi))