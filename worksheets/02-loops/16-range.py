print(*range(0,20))
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

print(*range(15))
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

#atlamali yazdirma(2 yerine istediginizi yazin)
print(*range(1, 26, 2))
# 1 3 5 7 9 11 13 15 17 19 21 23 25

#tersten alusturmak
print(*range(20, 0, -1))
#20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

#range ile loop
for i in range(1, 7):
  print(i)
# 1
# 2
# 3
# 4
# 5
# 6