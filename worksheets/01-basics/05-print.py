#Virgul ile ayirarak toplu bastirmak
print('Hello','world!')

# \n alt satir
print('Hello\nworld')
#Hello
#world

# \t bir tab bosluk birakir arada (normal tab 4 ama benim vscode tab 2 bosluk)
print('Hello\tworld')
#Hello  world
print('Hello\t\tworld')
#Hello    world

#!TYPE
a = 15
b = '15'
print(type(a))
#<class 'int'>
print(type(b))
#<class 'str'>

#!SEP Parametresi
print('Hello', 'world')
#Hello world
#Normalde bosluk olan yere sep parametresi ile custom isaret ayarlayabiliyoruz.
print('Hello', 'world', sep = '-')
#Hello-world
print('Hello', 'world', sep = '/')
#Hello/world
print('31','10','1991', sep='/')
#31/10/1991

#!Yildizli Parametreler
print('Python')
#Python
#Herbir parametreyi ayirarak boslukluk olarak gonderir
print(*'Python')
#P y t h o n
print(*'Python', sep='-')
#P-y-t-h-o-n
print(*'TBMM', sep='.')
#T.B.M.M.

#!Formatlama
print('{} {} {}'.format(3.1, 5.2, 6.5))
#3.1 5.2 6.5
c = 10
d = 5
print("{}+{}'nin toplami {}'dir".format(c,d,c+d))
#10+5'nin toplami 15'dir

#formattaki indexe gore formatlama
print('{1} {0}'.format('Yazar', 'Mucahid'))
#Mucahid Yazar

#kac tane float degerini alacagini ayarlariz
print('{:2f} {:4f}'.format('1.31233', '2.213213'))
#1.31 2.2132