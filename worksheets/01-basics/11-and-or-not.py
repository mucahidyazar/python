#MANTIKSAL BAGLACLAR
print(1 < 2); #True
print('Murat' == 'Murat') #True

#AND
#Hepsi dogruysa True, 1 tanesi yanlissa false doner
print(1 < 2 and 'Murat' == 'Murat')#True
print(1 < 2 and 'Murat' == 'Ali')#False

#OR
#Bir tanesi dahi dogruysa True, hepsi yanlissa False doner
print(1 > 2 or 'Murat' == 'Murat')#True
print(1 > 2 or 'Murat' == 'Ali')#False

#NOT
#basina geldigi seyi olumsuz sekilde degerlendirir. 
#Yani True'yu False yapar, False'yi True yapar
print(2 == 2) #True
print(not 2 == 2) #False
print(not 2 != 2) #True