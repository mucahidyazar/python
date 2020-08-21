print("""
  ***********************************************
  Kullanici Girisi
  ************************************************
""")

sys_kullanici_adi = 'mucahidyazar'
sys_parola = '05369120161'
giris_hakki = 3

while True:
  kullanici_adi = input('kullanici adi: ')
  parola = input('parola: ')
  if(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print('Kullanici adi hatali')
    giris_hakki-=1
  elif(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print('Parola hatali')
    giris_hakki-=1
  elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print('Kullanici adi ve Parola hatali')
    giris_hakki-=1
  else:
    print('Sisteme basari ile giris yapildi... Hos geldin {}'.format(kullanici_adi))
    break
  if giris_hakki == 0:
    print('Giris hakkiniz bitti')
    break
