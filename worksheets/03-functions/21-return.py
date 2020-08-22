# def toplama(a,b,c):
#   print('Toplamlari:',a+b+c)

#toplam = toplama(3,4,5) #NoneType Error #Cunku return yok

def toplama(a,b,c):
  return a+b+c
#returnden sonraki ayni blokdaki kodlar calismaz yapilacak islemler return den once yapilmali
def ikiylecarp(a):
  print('Result:',a*2) #Calisir
  return a*2
  print('Result:',a*2) #Calismaz

toplam = toplama(3,4,5) #12
print(ikiylecarp(toplam)) #12*2=24