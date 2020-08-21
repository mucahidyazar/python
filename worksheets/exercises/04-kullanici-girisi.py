print("""
  ***********************************************
  Kullanici Girisi
  ************************************************
""")


sys_kullanici_adi = 'mucahidyazar'
sys_parola = '05369120161'

kullanici_adi = input('Kullanici adi: ')
parola = input('Parola: ')

if kullanici_adi == sys_kullanici_adi and sys_parola != parola:
  print('Parola hatali...')
elif kullanici_adi != sys_kullanici_adi and sys_parola == parola:
  print('Kullanici adi hatali...')
elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
  print('Kullanici adi ve parola hatali')
else:
  print('Sisteme basarili bir sekilde giris yapildi')