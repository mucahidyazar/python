from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get('https://twitter.com/')
time.sleep(2)
girisYap = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[2]/a[2]')
girisYap.click()
time.sleep(2)

#!INPUT SECMEK
username = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
password = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

#!INPUTA YAZI EKLEMEK
username.send_keys('Develop89219495')
password.send_keys('1991Developer')

#!LOGIN BUTONUNU SECIP CLICK YAPARAK GIRIS YAPMAK
girisYap = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
girisYap.click()
time.sleep(2)

#!HASHTAG SEARCH ETMEK
searchArea = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
searchArea.send_keys('#yazilimayolver', Keys.ENTER) #Keys.ENTER => Entera basmasini saglar
time.sleep(2)

#!SELENIUM => ILERI ve GERI'ye GITMEK SAYFALARDA
#browser.back() => Geriye gider
#browser.next() => Ileriye gider
#time.sleep(2)

#!SAYFAYI ASAGIYA SCROLL ETMEK
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

#!TWEETLERI TOPLAMAK
tweets = []
elements = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div')

for i in elements:
  tweets.append(i.text)

#!TWEETLERI TXT DOSYASINA EKLEMEK
tweetsCount = 1

with open('tweets.txt', 'w', encoding='utf-8') as file:
  for tweet in tweets:
    file.write(str(tweetsCount)+'.\n' + tweet + '\n')
    file.write('--------------------------------\n')
    tweetsCount+=1

time.sleep(2)

browser.close()
