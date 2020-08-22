# Kendi Modüllerimizi Yazmak

#   1. Herhangi bir tane klasör oluşturuyoruz.
#   2. Modülümüz ve deneme Python dosyamız aynı dizinde olması gerektiği için 
#2 tane Python dosyasını da bu klasör altında oluşturuyoruz.
#   3. modul1.py ve deneme.py dosyası oluşturuyoruz.
#   4. modul1.py dosyasının içine istediğimiz kadar fonksiyonu yazıyoruz.
#   5. Son olarak da deneme.py dosyasının içinde bu modul1.py modülünü kullanıyoruz.

# Peki yazdığımız bir modülü her yerden kullanmak için ne yapacağız ? 
# Bunun için yazdığımız modul1.py dosyasının Python35/Lib klasörünün altına 
#atmamız gerekiyor. 
# Böylelikle bu modülü de math modülü gibi her dosyada kullanabiliriz.

#!Istersek kendi module umuzu Pythonun kurulu oldugu yerdeki lib'e atarak her yerden import edebiliriz.
# C:\Program Files\Python\Lib