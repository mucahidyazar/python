#arrayler gibidir fakat onlar gibi degistirilemezler
tuple1 = (1,2,3,4,5,6,7)
print(type(tuple1)) #<class 'tuple'>
tuple1[0] #1
tuple1[1] #2
tuple1[2] #3
tuple1[-1] #7
tuple1[-2] #6
tuple1[::-1] #(7,6,5,4,3,2,1)

#!Tuple Metodlari
tuple2 = (1,1,1,1,1,2,2,4,5)
#tuple in icinde kac tane 1 gectigini bulur. Count yerine istediginizi yazabilirsiniz.
print(tuple2.count(1)) #5
print(tuple2.count(5)) #1
#olmayan seyler icin 0 sonucunu verir
print(tuple2.count(10)) #0

#indexi bulmak
tuple3 = ('python', 'php', 'java', 'c')
print(tuple3.index('python')) #0
print(tuple3.index('java')) #2
print(tuple3.index('AngularJS')) #VALUEERROR

#!Degistirilemezler
tuple4 = (1,1,1,1,1,2,2,4,5)
#tuple4[0] = 0 #ERROR
#tuple4.remove(1) #ERROR

