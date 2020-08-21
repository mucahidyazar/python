# Problem 16
# Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

# Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

# İpucu: Basit düşünmeye çalışın.

print("""
  ***********************************************
  x'den y'ye kadar olan sayilardan sadece cift sayilar with list-comprehension

  Press C to quit
  Press Q to quit
  ************************************************
""")

while True:
  process = input('Please write a number starting the process : ')
  if process == 'q':
    break
  elif process == 'c':
    x = int(input('Please write a number for x : '))
    y = int(input('Please write a number for y : '))
    theNumbers = [i for i in range(x, y) if i%2==0]
    print(theNumbers)

