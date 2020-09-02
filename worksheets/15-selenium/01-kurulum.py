
#!SELENIUM
#pip install selenium

#!WEBDRIWER
#seleniumla browser acilip kullanilmasi icin bir webdriwer yuklemeliyiz
#geckodriver i mozilla icin indirip path e tanimliyoruz
#https://github.com/mozilla/geckodriver/releases
#https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

#!XPATH
#? //*[@id="topnav"]/div/div[1]/a[7]
#* //* =>html sayfasini simgeliyor
#* [@id="topnav"] => id si topnavi olani al diyor
#* /div divi al (Yukaridaki butun link icin topnav icindeki div anlaminda)
#* /div[1] => icindeki 1. divi al
#* /a[7] => 7. a elemanini al

#Browser console'da $x('xPathAdresi') yaparak o xpath e ait kac tane element var gorebiliriz
#$x('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[2]/a[2]')