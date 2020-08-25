
#!REDUCE
#MANTIK 12+18+20+10
from functools import reduce

def toplama(x,y):
  return x+y

toplam = reduce(toplama, [12,18,20,10])
print(toplam) #60



#!RESIM GOSTERMEK
# from IPython.display import Image
# Image(filename='reduce.jpg')



#*FAKTORIYEL HESAPLAMAK
#MANTIK 1*2*3*4*5*6*7
carpim = reduce(lambda x,y : x*y, [1,2,3,4,5,6,7])
print(carpim) #5040



#*MAX SAYI BULMAK
#MANTIK
# -2, 3
# 3, 9
# 9, 4
# 9, 65
# 65, 1
# ve 65 return olur
def maximum(x,y):
  if x>y:
    return x
  else:
    return y

max = reduce(maximum, [-2,3,9,4,65,1])
print(max) #95