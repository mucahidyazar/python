
#!INTERNETTEN VERI CEKMEK
#WINDOWS KURULUM
#*pip3 install beautifulsoup4
#*pip3 install requests

import requests
from bs4 import BeautifulSoup

url = 'https://www.sinanerdinc.com/'
response = requests.get(url)

htmlContent = response.content

soup = BeautifulSoup(htmlContent, "html.parser")

#HTML SAYFASININ KAYNAGINI GORUNTULER
#print(soup.prettify())

#*a etiketlerini bulmak / liste doner
#*print(soup.find_all('a'))
#* for i in soup.find_all('a'):
#*   print(i) #A etiketlerini alir
#*   print(i.get('href')) # a etiketlerinin href linklerini alir
#*   print(i.text) # a etiketlerinin icindeki textleri alir
#*   print('---------')

#!Classa gore secim
articles = soup.find_all('div', {'class':'posts-list'})
for x in articles:
  print(x)