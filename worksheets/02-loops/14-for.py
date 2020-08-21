liste1 = [2,3,6]

for el in liste1:
  print(el)
#2
#3
#6

liste2 = [2,3,6]
toplam = 0
for el in liste2:
  toplam+=el
  print('Toplam {}, Eleman {}'.format(toplam, el))
# Toplam 2, Eleman 2
# Toplam 5, Eleman 3
# Toplam 11, Eleman 6
print(toplam) #11

#!Sadece cift sayilari bulup tespit etmek ve print etmek
liste3 = [1,2,3,34,54,63,78]
for el in liste3:
  if el%2 == 0:
    print(el)

#!Demetler uzerinde gezinmek
demet1 = (1,2,3)
for dem in demet1:
  print(dem)
# 1
# 2
# 3

#!Stringler uzerinde gezinmek
string1 = 'Python'
for letter in string1:
  print(letter)
# P
# y
# t
# h
# o
# n

#!Array icindeki Arraylerde gezinmek
liste4 = [['ada', 26], ['ali',12], ['deniz', 25]]
for [name, age] in liste4:
  print(name, age)
# ada 26
# ali 12
# deniz 25

#!Array icindeki Tuplelarda gezinmek
liste4 = [('ada', 26), ('ali',12), ('deniz', 25)]
for (name, age) in liste4:
  print(name, age)
# ada 26
# ali 12
# deniz 25

#!Dictionarylerde gezinme for loopu ile
dictionary1 = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5
}
#keysleri array olarak almak
print(dictionary1.keys()) #dict_keys(['one', 'two', 'three', 'four', 'five', 'six'])
for el in dictionary1.keys():
  print(el)
# one
# two
# three
# four
# five
#valuesleri almak
print(dictionary1.values()) #dict_values([2, 2, 3, 4, 5, 6])
for el in dictionary1.values():
  print(el)
# 1
# 2
# 3
# 4
# 5
#her bir sozluk elemanini liste icinde demet olarak tutmak
print(dictionary1.items()) #dict_items([('one', 2), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6)])
for (x, y) in dictionary1.values():
  print(x, y)
# one 1
# two 2
# three 3
# four 4
# five 5