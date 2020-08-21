# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

print("""
  ***********************************************
  Is this a 'Armstrong' number?

  Press Q to quit
  ************************************************
""")


while True:
  process = input('Write a number...')
  if process == 'q':
    break

  processUpper = len(process)
  total = 0
  for x in process:
    total += int(x)**processUpper
  if total == int(process):
    print('This number ({}) is a Armstrong number'.format(total))
    
  
