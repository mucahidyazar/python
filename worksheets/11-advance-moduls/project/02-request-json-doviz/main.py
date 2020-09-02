import requests
import sys

#&symbols=USD,AUD,CAD,PLN,MXN&format=1
url = 'http://data.fixer.io/api/latest?access_key=e32e9e777d060c5588ed069ac73839e3&base='

birinciDoviz = input('Birinci Doviz : ').upper()
ikinciDoviz = input('Ikinci Doviz : ').upper()
miktar = float(input('Miktar '))

response = requests.get(url + '&symbols=' + birinciDoviz + ',' + ikinciDoviz)

#Json olarak donen veriyi json olarak yakalamak
jsonVerisi = response.json()

print(jsonVerisi) #{'success': True, 'timestamp': 1598504645, 'base': 'EUR', 'date': '2020-08-27', 'rates': {'TRY': 8.703056}}
print(jsonVerisi['rates']) #{'TRY': 8.703056}
print(jsonVerisi['rates'].keys())
print(list(jsonVerisi['rates'].keys())[0])

try:
  birinciDovizKacIkinciDoviz = jsonVerisi['rates'][ikinciDoviz] / jsonVerisi['rates'][birinciDoviz]
  total = birinciDovizKacIkinciDoviz * miktar
  print('{} {} {} {} \'sidir'.format(miktar, list(jsonVerisi['rates'].keys())[0], total, list(jsonVerisi['rates'].keys())[1]))
except:
  #Hata gondermek eger api dogru calismaz ise
  sys.stderr.write('Lutfen para birimlerini dogru girin')
  sys.stderr.flush()