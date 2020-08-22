liste1 = [1,2,3,4,5]
liste2 = [i*2 for i in liste1] #2,4,6,8,10 #*list-comprehension

def ikiylecarp(x):
  return x*2
print(ikiylecarp(3)) #6
#LAMBDA ILE yukaridaki fonksiyonun yaptigi islemin aynisini yapariz
ikiylecarpLambda = lambda x : x * 2
print(ikiylecarpLambda(3)) #6

def toplama(x,y,z):
  return x+y+z
print(toplama(5,6,9))#20
#LAMBDA ILE
toplama2 = lambda x,y,z : x + y + z
print(toplama2(1,5,8))#14

def tersCevir(s):
  return s[::-1]
print('Ters') #sreT
#LAMBDA ile
ters = lambda s : s[::-1]
print(ters('Python')) #nohtyP

def cifTek1(sayi):
  return sayi % 2 == 0
print(cifTek1(14)) #True
print(cifTek1(151)) #False
cifTek2 = lambda sayi : sayi % 2 == 0
print(cifTek2(14)) #True
print(cifTek2(151)) #False