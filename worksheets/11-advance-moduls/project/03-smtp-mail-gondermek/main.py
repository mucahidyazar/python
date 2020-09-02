import smtplib
from email.mime.multipart import MIMEMultipart #Mail yapisi
from email.mime.text import MIMEText ##Mesaj govdesini olusturacak yani mailde ne yazacagi
import sys #hatalari bastiracagiz

mesaj = MIMEMultipart()
mesaj['from'] = 'developermucahidyazar@gmail.com'
mesaj['to'] = 'developermucahidyazar@gmail.com'
mesaj['Subject'] = 'SMTP Mail Gonderme'

yazi = """
  Smtp ile mail gonderiyorum

  Mucahid YAZAR
"""

mesajGovdesi = MIMEText(yazi, 'plain') #'plain' mesaj yapisi

mesaj.attach(mesajGovdesi)

try:
  mail = smtplib.SMTP('smtp.gmail.com', 587) #Gamil'in server ve porta baglanmak
  mail.ehlo() #smtp serverina kendimizi tanitip baglaniyoruz
  mail.starttls() #maillerimizin encrypt edilmesi sifrelenmesi icin
  mail.login('developermucahidyazar@gmail.com', '05369120161') #smtp login olmak
  mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())

  print('Mail basariyla gonderildi...')

  mail.close() #smtp serveriyla baglantiyi kesmek
except:
  sys.stderr.write('Bir sorun olsutu!')
  sys.stderr.flush() #Aniden ekrana basilmasini soyleriz












