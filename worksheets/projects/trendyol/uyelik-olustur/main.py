from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #HOVER ICIN
import time
import random
from names import getNames

amount = int(input('How many accounts do you want to create? #'))

names = getNames()

for process in range(1,amount+1):

  browser = webdriver.Firefox()
  browser.get('https://www.trendyol.com/')

  time.sleep(3)
  try:
    addCloseButton = browser.find_element_by_css_selector('a.fancybox-item.fancybox-close')
    if addCloseButton:
      addCloseButton.click()
  except:
    pass
  time.sleep(2)
  accountBtn = browser.find_element_by_xpath('//*[@id="accountBtn"]')
  accountBtn.click()
  time.sleep(2)
  kayitOlBtn = browser.find_element_by_xpath('//*[@id="foorterMain"]/a')
  kayitOlBtn.click()
  time.sleep(2)

  emailInput = browser.find_element_by_css_selector('input.authentication-input.email')
  passwordInput = browser.find_element_by_css_selector('input.authentication-input.password')
  acceptAccount = browser.find_element_by_css_selector('.membership-policy .checkbox')
  registerBtn = browser.find_element_by_id('registerSubmit')

  username = names[random.randint(0,len(names))]+names[random.randint(0,len(names))]+str(random.randint(100000,999999))+'@gmail.com'
  with open('users.txt', 'a', encoding='utf-8') as userDatas:
    userDatas.write(username + ' asdzxc123\n')
  emailInput.send_keys(username)
  passwordInput.send_keys('asdzxc123')
  acceptAccount.click()
  time.sleep(1)
  registerBtn.click()

  time.sleep(3)
  try:
    notificationPopupClose = browser.find_element_by_xpath('//*[@id="modal-root"]/div/div/div[1]')
    if notificationPopupClose:
      notificationPopupClose.click()
  except:
    pass

  time.sleep(2)
  accountBtn = browser.find_element_by_css_selector('li.login-register-button-container')
  hover = ActionChains(browser).move_to_element(accountBtn)
  hover.perform()

  time.sleep(2)
  logoutBtn = browser.find_element_by_xpath('//*[@id="logged-in-container"]/div/div[9]')
  logoutBtn.click()

  browser.close()