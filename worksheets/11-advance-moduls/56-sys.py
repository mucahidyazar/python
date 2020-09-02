
#!SYS 
#Python Sistemine ozgu ozellikleri kullaniriz

import sys

#print(dir(sys)) => sys methodlarini gormek

#!EXIT() => Programi aniden sonlandirir yani altindaki kodlar calismaz
#*a = int(input('A:'))
#*b = int(input('B:'))
#*sys.exit()
#*c = int(input('C:'))

#!STDERR => Hata MEsajlari gonderebiliriz
#* sys.stderr.write('Bu bir hata mesajidir')
#* sys.stderr.flush() #Bu bir hata mesajidir

#!ARGV
print(sys.argv)
for i in sys.argv:
  print(i)
#Eger komut satirindan bu sekilde cagirirsak #*python 56-sys.py
# ['56-sys.py']
# 56-sys.py
#Eger komut satirindan bu sekilde cagirirsak #*python 56-sys.py 1 2 3
# ['56-sys.py', '1', '2', '3']
# 56-sys.py
# 1
# 2
# 3