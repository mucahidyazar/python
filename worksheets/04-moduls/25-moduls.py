#Pythonda her bir dosya moduldur
#Moduller bizim veya baskalari tarafindan yazilmis hazir package lerdir.
#Python'u bilgisayari kurdugumuzda bazi hazir moduller Python ile birlikte geliyor bazilarida internete Github'a vs yukleniyor kullanicilar tarafidnan

#!Python ile birlikte kurulan moduller
#Bu moduller Pythonu kurdugumuz yerde Lib kulasoru icindedir. 
#*Mesela bende => C:\Program Files\Python\Lib

#!Github'da olanlar
#Google'a Github Python Moduls yazdigimizda cikan sonuclarda goruruz.

#!Modul Kullanimi
#!Yontem 1 - import moduleName
import math

#Module'deki methodlari gormek
#*print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 
# 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

#Module methodlari ne ise yarar bu kodla ogrenebiliriz
#*help(math)

#Faktoriyel bulma yapabiliriz mesela math'in factorial methodu ile
print(math.factorial(5)) #120
print(math.factorial(3)) #6

print(math.floor(5.6)) #5
print(math.floor(3.1)) #3
print(math.floor(93.9)) #93

#!math modulunu farkli isimle kullanmak
import math as matematik
print(matematik.factorial(5)) #120

#!Yontem2 - from moduleName import *
#ModuleName'e sahip moduledeki methodlardan * ile hepsini secip import ile edip dahil ediyoruz
#Bu kullanimda module adi math'i kullanmadan direk kullanabiliriz methodlarimizi
from math import *
print(math.factorial(5)) #120
print(factorial(10)) #3628800

#!Ozel methodlari import etmek sadece
from math import floor,ceil
print(floor(5.6)) #5
print(floor(3.1)) #3
print(ceil(5.6)) #6
print(ceil(3.1)) #4
