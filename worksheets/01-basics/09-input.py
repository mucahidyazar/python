#terminalde calistirdigimiz zaman bizden bir sayi isteyecek
input()

#Terminalde calistiginda icindekini gosterecek ve ayrica inputa bir seyler yazilacabilecek
input('Lutfen bir sayi giriniz :')

#!
a = input('Lutfen bir sayi giriniz : ')
print('Kullanicinin girdigi deger : ', a) #Kullanicinin girdigi deger :  50
print(a*3) #353535
print(type(a)) #<class 'str'>
print(int(a)*3) #105

a = int(input('First number : '))
b = int(input('Second number : '))
c = int(input('Third number : '))
print('Toplamlari ', a+b+c) #Toplamlari  35