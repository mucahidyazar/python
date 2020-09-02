def baglantiYap(metin):
    liste = {"ı": "i",
             "I": "i",
             "Ç": "c",
             "ç": "c",
             " ": "-",
             "ş": "s",
             "Ş": "s",
             "Ğ": "g",
             "ğ": "g",
             "Ü": "u",
             "ü": "u",
             "Ö": "o",
             "ö": "ö"}

    for karakter in liste:
        metin = metin.replace(karakter, liste[karakter])
    return metin.lower()

# firstNames = []
# lastNames = []


# with open('names.txt', 'r', encoding='utf-8') as file:
#   for x in file:
#     firstNames.append(baglantiYap(x.replace('\n', '')))
#     lastNames.append(baglantiYap(x.replace('\n', '')))

import random

def getName():
  names = []
  with open('names.txt', 'r', encoding='utf-8') as file:
    for x in file:
      names.append(baglantiYap(x.replace('\n', '')))
  return names[random.randint(0,len(names))]

def getNames():
  names = []
  with open('names.txt', 'r', encoding='utf-8') as file:
    for x in file:
      names.append(baglantiYap(x.replace('\n', '')))
  return names
