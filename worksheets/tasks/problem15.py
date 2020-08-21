# Problem 15
# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

print("""
  ***********************************************
  x'den y'ye kadar olan sayilardan sadece z'ye bolunen sayilar

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
    z = int(input('Please write a number for z : '))
    theNumbers = []
    for i in range(x, y):
      if i % z == 0:
        theNumbers.append(i)
    print(theNumbers)

