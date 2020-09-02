
#!Iterator sinifi olusturma ornegi
class Kuvvet3():
  def __init__(self, max = 0):
    self.max = max
    self.kuvvet = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.kuvvet <= self.max:
      sonuc = 3 ** self.kuvvet

      self.kuvvet += 1

      return sonuc
    else:
      raise StopIteration

kuvvet = Kuvvet3(6)

iterator = iter(kuvvet)

print(next(iterator)) #3^0 => 1
print(next(iterator)) #3^1 => 3
print(next(iterator)) #3^2 => 9
print(next(iterator)) #3^3 => 27
print(next(iterator)) #3^4 => 81

for i in kuvvet:
  print(i)
# 243
# 729

#! Generator Ornegi - Fibonacci Ornegi
def fibonacci():
  a = 1
  b = 1
  yield a
  yield b

  while True:
    a,b = b,a+b
    yield b

for sayi in fibonacci():
  if sayi > 100000:
    break
  print(sayi)
