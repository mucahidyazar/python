def greeting1 (name):
  print('Hi',name)

greeting1('Mucahid') #Hi Mucahid
#Eger parametre tanimlamazsak asagidaki gibi ERROR aliriz.
#greeting1() #Error

#Fakat default value tanimlarsak ERROR almayiz bos biraktigimizda
def greeting2 (name='Isimsiz'):
  print('Hi',name)
greeting2() #Hi Isimsiz

def showInformation(firstName='Unknown', lastName='Unknown', number='Unknown'):
  print('First Name:', firstName, 'Last Name:', lastName, 'Number:', number)
showInformation() #Unknown Last Name: Unknown Number: Unknown
#!Sadece istedigimiz argumenti gondermek
showInformation(number=25) #Unknown Last Name: Unknown Number: 25

#!!!Bu sayede 1 parametre alan fonksiyonlara 1 den fazla argument gonderdigimizde 
#!o gonderdigimiz argumentler bize tupple olarak doner 
#!ve biz bununla tuple 'i kullanarak asagidaki gibi degisik islemler yapabiliriz
def toplama(a,b,c):
  print('Toplam', a+b+c)
#toplama(1,2,3,4) #Error
def esnekToplama1(*a):
  print(a)
esnekToplama1(1,2,3) #(1,2,3) #a bize bir Tupple olarak doner

def esnekToplama2(*a):
  toplam = 0
  for i in a:
    toplam += i
  print(toplam)
esnekToplama2(1,2,3) #6
esnekToplama2(11,2,32) #45