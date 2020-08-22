#Basit bir class tanimi
class Araba():
  model = 'Renault Megane'
  color = 'Silver'
  power = 750

araba1 = Araba()
araba2 = Araba()

print(araba1.model) #Renault Megane
print(araba2.model) #Renault Megane
print(araba2.power) #750
print(Araba.model) #Renault Megane
print(Araba.power) #750


#! __init__() => Herhangi bir classimizda bunu tanimlarsak Python'a 
#! sen bunu tanimlama ben tanimlayip kendi degerlerimde olusturacagim objemizi diyebiliyoruz.
#* print(dir(araba1)) 
#Bunu yaptrighiniz zaman Python tarafindan class yapisinda Araba'ya tanimlanmis 
#ve ondanda olusturulan objectlere tanimlanmis hazir methodlari gorebilirsiniz.
#Bunlardan biriside __init__() dir.

#Buradaki self aslinda NewAraba class'idir. Biz busayede init ile Objectlerimizi
#sekillendirirken self ile bunlari yakalayip degerlerimizi bunlara atayabilecegiz
class NewAraba():
  def __init__(self, model = 'No information', power = 'No information', color = 'No information'):
    print('Init fonksiyonu cagrildi')
    self.model = model
    self.power = power
    self.color = color
araba3 = NewAraba('Renault Megane', 750, 'Silver')
araba4 = NewAraba('Renault Clio', 450, 'Red')
print(araba3.color) #Silver
print(araba4.color) #Red