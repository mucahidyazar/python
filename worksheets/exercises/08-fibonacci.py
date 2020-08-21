print("""
  ***********************************************
  Fibonacci Serisi
  ***********************************************

  Nedir?
  yeni bir sayiyi onceki iki sayinin toplami seklinde olusturur
  1,1,2,3,5,8,13,21,34........

""")

a = 1
b = 1

fibonacci = [a,b]

for i in range(20):
  a,b = b,a+b
  fibonacci.append(b)
print(fibonacci)
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
