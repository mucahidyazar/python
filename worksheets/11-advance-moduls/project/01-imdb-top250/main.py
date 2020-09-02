import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

response = requests.get(url)

#print(response)

htmlContent = response.content

soup = BeautifulSoup(htmlContent, 'html.parser')

#print(soup.prettify()) #Sayfa iskeleti

siralama = float(input('Bir paun degeri giriniz? (1-10 arasinda) #'))

basliklar = soup.find_all('td', { 'class': 'titleColumn' })
ratingler = soup.find_all('td', { 'class': 'ratingColumn imdbRating' })
print(len(basliklar)) #250
print(len(ratingler)) #250

for baslik,rating in zip(basliklar,ratingler):
  baslik = baslik.text
  rating = rating.text

  baslik = baslik.strip()
  baslik = baslik.replace("\n", "")
  rating = rating.strip()
  rating = rating.replace("\n", "")
  rating = float(rating)

  if rating > siralama:
    print('Film ismi : {} Film Puani : {}'.format(baslik, rating))
  else:
    continue

  print('----------------------')

# for i in basliklar:
#   print(i)
#   # <td class="titleColumn">
#   #   250.
#   #   <a href="/title/tt0050613/" title="Akira Kurosawa (dir.), Toshirô Mifune, Minoru Chiaki">Kumonosu-jô</a>
#   #   <span class="secondaryInfo">(1957)</span>
#   # </td>
#   print(i.text)
#   # 250.
#   #   Kumonosu-jô
#   # (1957)
#   print('----------------------')

