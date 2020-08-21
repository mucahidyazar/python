# Problem 2
# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

boy = int(input('Boy(cm) : ')) / 100
kilo = int(input('Kilo(kg) : '))

print('Beden kitle indeksi : ', kilo / (boy * boy))