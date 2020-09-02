from selenium import webdriver
import time
import loginInfo

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')
time.sleep(2)

usernameInp = browser.find_element_by_name('username')
passwordInp = browser.find_element_by_name('password')
girisYapBtn = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

usernameInp.send_keys('kabusof0004')
passwordInp.send_keys('05369120161')
girisYapBtn.click()
time.sleep(5)

addPanel = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
addPanel.click()
time.sleep(2)

profileIcon = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]')
profileIcon.click()
time.sleep(2)

userIcon = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
userIcon.click()
time.sleep(2)

followingLink = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
followingLink.click()
time.sleep(2)

jscommand = """
  const followers = document.querySelector('.isgrP');
  followers.scrollTo(0, followers.scrollHeight);
  const lenOfPage = followers.scrollHeight;
  return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

time.sleep(2)
                                                    
followingUsers = browser.find_elements_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li/div/div[1]/div[2]/div[1]/span/a')

followingList = []
for followingUsername in followingUsers:
  followingList.append(followingUsername.text)

with open('followings.txt', 'w', encoding='utf-8') as file:
  for following in followingList:
    file.write(following + '\n')

browser.close()