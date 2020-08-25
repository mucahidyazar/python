#https://www.tutorialspoint.com/python3/python_strings.htm

#!UPPER
#Stringin butun karakterlerini buyuk harfe cevirir
print('python'.upper()) #PYTHON


#!LOWER
#Stringin butun karakterlerini kucuk harfe cevirir
print('PYTHON'.lower()) #python

#!REPLACE
#a karakterlerini o ya cevirmek
print('Herkes ana baba baci gardas'.replace('a', 'o')) #Herkes ono bobo boci gordos
print('Python Programlama Dili'.replace(' ','-')) #Python-Programlama-Dili
print('Kunduz'.replace('duz', 'zum')) #Kunzum

#!startswith(x)
#string x ile basliyorsa True, baslamiyorsa False doner
print('Python'.startswith('a')) #False
print('Python'.startswith('p')) #False
print('Python'.startswith('P')) #True

#!endswith(x)
#string x ile bitiyorsa True, bitmiyorsa False doner
print('Python'.endswith('s')) #False
print('Python'.endswith('N')) #False
print('Python'.endswith('on')) #True

#!SPLIT
#Bolerek Array olarak toplariz
liste = 'Python Programlama Dili'.split(' ')
print(liste) #['Python', 'Programlama', 'Dili']

#!JOIN
#Listenin elemanlarini birlestirir
liste = ["21","02","2014"]
print("/".join(liste)) #21/02/2014
liste2 = ["T","B","M","M"]
print(".".join(liste2)) #T.B.M.M

#!STRIP(x)
#Stringin basinda ve sonunda bulunan x degerlerini siler
print('------python------'.strip("-")) #python

#!LSTRIP(x)
#Stringin sadece basinda x degerlerini siler
print('------python------'.lstrip("-")) #python------

#!RSTRIP(x)
#Stringin sadece sonunda x degerlerini siler
print('------python------'.rstrip("-")) #------python   

#!COUNT(x)
#Stringin icindeki x degerini sayar
print('ada kapisi yandan carkli'.count('a')) #6
print('ada kapisi yandan carkli'.count(' ')) #3
#!COUNT(x, index)
#stringin icindeki x degerini index den baslayarak sayar
print('ada kapisi yandan carkli'.count('a', 2)) #5

#!FIND(x)
#x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
print('araba'.find('a')) #0
print('araba'.find('r')) #1
print('araba'.find('b')) #3
print('araba'.find('s')) #-1

#!RFIND
#x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
print('araba'.rfind('a')) #4
print('araba'.rfind('s')) #-1








