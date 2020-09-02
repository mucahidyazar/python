import requests
from bs4 import BeautifulSoup

url = 'https://www.trendyol.com/Hesabim/IndirimKuponlari'
response = requests.get(url)

htmlContent = response.content

soup = BeautifulSoup(htmlContent, 'html.parser')

coupons = soup.find_all('div', { 'class': 'couponBoxContainer' })
for x in coupons:
  print(x)
  print('------------------')