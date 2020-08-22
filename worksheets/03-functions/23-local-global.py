
#!LOCAL
def function1():
  a = 10 #LOCAL VARIABLE
  print(a)
function1() #10

#!GLOBAL
b = 5 #GLOBAL VARIABLE
def function2():
  print(b)

#Hata verir cunku function calistiginda henuz c degiskeni olusturulmamisti
def function3():
  print(c) #ERROR
c = 5 #GLOBAL VARIABLE

#!Fonksiyon icinde Globaldeki ayni isime sahip bir degisken yazildiginde 
#!yeni bir degisken olusturulur, Globaldeki degisken degismez
d = 5 #GLOBAL VARIABLE
def function4():
  d = 2
  print(d)
function4() #2
print(d) #5

#!Globaldeki degiskeni degistirmek icin
e = 5 #GLOBAL VARIABLE
def function5():
  global e
  e = 3
  print(e)
function5() #3
print(e) #3

#!IF WHILE icindeki degiskenler LOCAL mi? HAYIR
#IF ve WHILE icinde tanimlanan degiskenler GLOBAL olarak tanimlanir.
#GLOBAL degiskenler sadece FUNCTINOS ve OBJECTLERE ozgudur.
if True:
  e = 4
  print(e)
print(e) #4
