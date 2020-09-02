
#!PILLOW - pillow.readthedocs.io
#Ilk once module muzu yukluyoruz
#*pip3 install Pillow

from PIL import Image,ImageFilter

image = Image.open('kuş.jpg')

#*image.show() #Resmin windows uzerinde ki resim gostericisiyle acilmasini saglar

#*image.save('kuş2.jpg') #Resmi ayni konumda verilen ad ile kopyalar

#*image.rotate(180).save('kuş3.jpg') #180 derece cevirip kaydederiz

#*image.convert(mode = 'L').save('kuş4.jpg') #Resmi siyah beyaz resime cevirir

#! 1920*1200 px resimi 960*600 px'e donusturur
#* newSizes = (960,600)
#* image.thumbnail(newSizes)
#* image.save('kuş5.jpg')

#! Resimi belirlenen efektte 5 siddetinde ayarlariz yani blurlama
#*image.filter(ImageFilter.GaussianBlur(5)).save('kuş6.jpg')
#*image.filter(ImageFilter.GaussianBlur(10)).save('kuş7.jpg')

kirpilacakAlan = (340,0,950,600)
image.crop(kirpilacakAlan).save('kuş8.jpg')






