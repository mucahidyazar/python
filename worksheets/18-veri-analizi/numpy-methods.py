# numpy Array Yapisi ve Array Islemleri
data_list = [1,2,3] #Tek boyutlu array

# insnalar genel olarak np ile kullaniyor
import numpy as np

arr = np.array(data_list)
print(arr) #[1 2 3]
print(arr[0]) #1
print(arr[2]) #3

data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
arr2 = np.array(data_list2)
print(arr2)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
print(arr2[2,2]) #90
print(arr2[0,1]) #20
#print(arr2[5,5]) #Olmadıgı icin error verir

#!ARANGE #10 ile 20 arasindaki arraylerden array olusturur
arr4 = np.arange(10,20)
print(arr4) #[10,11,12,13,14,15,16,17,18,19]

#3 er atlayarak arange etmek
arr5 = np.arange(0,10,3) #[0,3,6,9]
print(arr5)

#ZEROS Her eleman 0 dan olusur
arr6 = np.zeros(5)
print(arr6) #[0., 0., 0., 0., 0., 0.]

arr7 = np.ones(3)
print(arr7) #[1., 1., 1., 1., 1.]

#Martis olusturarak depolama
arr8 = np.zeros((2,2)) #2x2 lik matris olusturur
print(arr8)
# [[0., 0.]
#  [0., 0.]]


#!LINSPACE
arr9 = np.linspace(0,100,5) #0-100 arasindaki parcalari 5 esit parcaya bolup 5 parca li arrayolusturur
print(arr9) #[0., 25., 50., 75., 100.]
arr10 = np.linspace(0,1,6)
print(arr10) #[0., 0.2, 0.4, 0.6, 0.8, 1.]

#! EYE - BIRIM MATRIS
arr11 = np.eye(2)
print(arr11)
# [[1., 0.],
#  [0., 1.]]
arr12 = np.eye(3)
print(arr12)
# [[1., 0., 0.],
#  [0., 1., 0.],
#  [0., 0., 1.]]

#!RANDOM
np.random.randint(0,10) #0-10 arasinda rastgele integer sayi olusturur

arr13 = np.random.randint(1,10,5) #1-10 arasinda 5 tane rastgele sayiyi array olarak doner
print(arr13) #[1,7,2,8,9]

#!RAND
arr14 = np.random.rand(5) #5 tane 0 ile 1 arasinda olan float sayiyi array icinde doner
print(arr14) #[0.52062566, 0.21515121, 0.865145445, 0.54151223, 0.23165355]

#!RANDN #Hem + hem - olarak 0 ile 1 arasindaki sayilari array olarak doner
arr15 = np.random.randn(5)
print(arr15) #[-0.52062566, -0.21515121, 0.865145445, -0.44151223, 6.23165355]


#!RESHAPE - SIRALI MATRIS
arr16 = arr.reshape(2,2)
print(arr16)
# [[0,1],
#  [2,3]]
arr17 = arr.reshape(3,3)
print(arr17)
# [[0,1,2],
#  [3,4,5],
#  [6,7,8]]
#arr.reshape(4,3) #ERROR

#!OTHER METHODS
arr18 = np.random.randint(1,100,10)
print(arr18.max()) #En buyuk degeri alir
print(arr18.min()) #En kucuk degeri alir
print(arr18.sum()) #Tum arrayin toplamini alir
print(arr18.mean()) #Tum arrayin ortalamasini alir
print(arr18.argmax()) #en buyuk sayinin indexini al
print(arr18.argmin()) #en kucuk sayinin indexini al