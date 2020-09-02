import numpy as np

arr1 = np.arange(1,10)
print(arr1) #[1,2,3,4,5,6,7,8,9]
print(arr1[0]) #1
print(arr1[2]) #3
print(arr1[3]) #4
print(arr1[8]) #9
print(arr1[:4]) #[1,2,3,4]
print(arr1[::2]) #[1,3,5,7,9]

arr1[:3] = 25
print(arr1) #[25,25,25,4,5,6,7,8,9]


#! REFERENCE and COPY
#!arr2 yi arr1'den reference ile kopyalarsak ve arr2 yi degistirirsek arr1 de degisecektir
arr1 = np.arange(1,10)
print(arr1) #[1,2,3,4,5,6,7,8,9]
arr2 = arr1
print(arr2) #[1,2,3,4,5,6,7,8,9]
arr2[:3] = 100
print(arr1) #[100,100,100,4,5,6,7,8,9]
print(arr2) #[100,100,100,4,5,6,7,8,9]

#!Kopyalayarak olusturursak arr2 degistiginde arr1 degismez
arr1 = np.arange(1,10)
print(arr1) #[1,2,3,4,5,6,7,8,9]
arr2 = arr1.copy()
print(arr2) #[1,2,3,4,5,6,7,8,9]
arr2[:3] = 100
print(arr1) #[1,2,3,4,5,6,7,8,9]
print(arr2) #[100,100,100,4,5,6,7,8,9]


arr3 = np.arange(1,21)
arr3 = arr3.reshape(5,4)
print(arr3)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]
print(arr3[0,0]) #1
print(arr3[:,:2])
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]
#  [13 14]
#  [17 18]]
print(arr3[:3,:3])
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11]]
print(arr3[:2])
print(arr3[:2,:])
# [[1 2 3 4]
#  [5 6 7 8]]

#!FILTER
arr4 = np.arange(1,11) #[1 2 3 4  5  6  7  8  9 10]
print(arr4 > 3) #[False False False  True  True  True  True  True  True  True]
print(arr4[arr4 > 3]) #[ 4  5  6  7  8  9 10]

arr5 = np.array([10,20,30,40,50,60])
arr6 = np.array([1,2,3,4,5,6])
print(arr5 + arr6) #[11 22 33 44 55 66]
print(arr5 + 10) #[ 20  30  40 50 60 70] #Herbir eleman 10 ile toplanir
print(arr5 - arr6) #[ 9 18 27 36 45 54]
print(arr5 * arr6) #[ 10  40  90 160 250 360]

#!SQRT
arr5 = np.array([10,20,30,40,50,60])
print(np.sqrt(arr5)) #[3.16227766 4.47213595 5.47722558 6.32455532 7.07106781 7.74596669]
