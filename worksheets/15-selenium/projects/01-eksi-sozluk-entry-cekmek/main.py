#Web driveri dahil etmek
from selenium import webdriver
import random #random sayfa numarasi olusturmak icin
import time #web sayfamizin kac saniye aktif kalacagini soylemek icin

#browser olusturmak
browser = webdriver.Firefox()

#browserdan siteyi acmak
url = 'https://eksisozluk.com/mustafa-kemal-ataturk--34712?p='

pageCount = 1
entries = []
while pageCount <= 3:
  randomPage = random.randint(1,2000)
  newUrl = url+str(randomPage)
  browser.get(newUrl)
  elements = browser.find_elements_by_css_selector('.content')
  for i in elements:
    entries.append(i.text)
  time.sleep(1)
  pageCount+=1

with open('entries.txt', 'w', encoding='utf-8') as file:
  for entry in entries:
    file.write(entry + '\n')
    file.write('****************\n')
# for i in entries:
#   print(i)
#   print('---------')

browser.close()

#.content classina sahip elementsleri secer ve array olarak bize geri dondurur
# elements = browser.find_elements_by_css_selector('.content')
# for x in elements:
#   print(x.text)
#   print('------------')