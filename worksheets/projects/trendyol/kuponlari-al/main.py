from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #HOVER ICIN
import time
import random

browser = webdriver.Firefox()
browser.get('https://www.trendyol.com/')

time.sleep(2)
try:
  addCloseButton = browser.find_element_by_class_name('fancybox-close')
  addCloseButton.click()
except:
  pass

time.sleep(2)
accountBtn = browser.find_element_by_xpath('//*[@id="accountBtn"]')
accountBtn.click()

time.sleep(2)
emailInput = browser.find_element_by_css_selector('input.authentication-input.email')
passwordInput = browser.find_element_by_css_selector('input.authentication-input.password')
loginBtn = browser.find_element_by_id('loginSubmit')

emailInput.send_keys('mucahidyazar@gmail.com')
passwordInput.send_keys('123456789a')
loginBtn.click()

time.sleep(3)
try:
  notificationPopupClose = browser.find_element_by_xpath('//*[@id="modal-root"]/div/div/div[1]')
  notificationPopupClose.click()
except:
  pass

time.sleep(2)
accountBtn = browser.find_element_by_css_selector('li.login-register-button-container')
hover = ActionChains(browser).move_to_element(accountBtn)
hover.perform()

time.sleep(2)
couponsBtn = browser.find_element_by_xpath('//*[@id="logged-in-container"]/div/div[5]')
couponsBtn.click()

time.sleep(2)
couponNames = browser.find_elements_by_xpath('//*[@id="account"]/div[2]/div[2]/div[2]/div/div/div[1]/span')
couponDiscounts = browser.find_elements_by_xpath('//*[@id="account"]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/label')

coupons = list()
for couponName in couponNames:
  coupons.append({
    'couponName': couponName.text
  })
for x in range(0,len(couponNames)):
  coupons[x]['couponDiscount'] = couponDiscounts[x].text
with open('coupons.txt', 'w', encoding='utf-8') as file:
  for coupon in coupons:
    file.write(coupon['couponName'] + ' ' + coupon['couponDiscount'] + '\n')

browser.close()