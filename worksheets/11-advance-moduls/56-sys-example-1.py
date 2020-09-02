import sys

def kokBulma(a,b,c):
  delta = b ** 2 - 4 * a * c

  if delta < 0:
    print('Reel Kok Yok')
  else:
    x1 = (-b - delta ** 0.5) / (2*a)
    x2 = (-b + delta ** 0.5) / (2*a)
    return (x1,x2)

if len(sys.argv) == 4:
  print('Kok bulma', kokBulma(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
  sys.stderr.write('Lutfen dogru degerler girin')
  sys.stderr.flush()

#! Bunu yazdigimiz zaman => python 56-sys-example-1.py 1 2 1
# Kok bulma (-1.0, -1.0)