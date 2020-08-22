#print() #Example for functions

#def functionName (parametre1, parametre2...):
  #function blogu
  #Yapilacak islemler
  #donus degeri

def greeting ():
  print('Hi')
  print('How are you')

greeting()
# Hi
# How are you

#greeting('New Argument') #TypeError: greeting() takes 0 positional arguments but 1 was given

def greetingWithLanguage(parametre):
  print(parametre)
greetingWithLanguage('Selam') #Selam
greetingWithLanguage('Hi') #Hi
greetingWithLanguage('Hola') #Hola

def sum(a,b,c):
  print('Toplam :', a+b+c)

sum(1,99,22) #Toplam : 122

#Faktoriyel Hesaplama with Functions
def faktoriyel(sayi):
  faktoriyel = 1
  if(sayi == 0 or sayi == 1):
    print('Faktoriyel',faktoriyel)
  else:
    while(sayi >= 1):
      faktoriyel *= sayi
      sayi -= 1
  print(faktoriyel)
faktoriyel(5) #120
faktoriyel(1) #1
faktoriyel(8) #40320
