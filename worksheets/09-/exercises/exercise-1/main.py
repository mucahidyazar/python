class Dosya():
  def __init__(self):
    with open('metin.txt', 'r', encoding='utf-8') as file:
      dosya_icerigi = file.read()

      #metindeki tum kelimeleri array halinde almak
      kelimeler = dosya_icerigi.split() #' ' ile ayirir hicbirsey yazmazsak
      self.sade_kelimler = list()

      #Nokta Virgul Bosluk ve Alt satirlari kelimelerden silmek
      for i in kelimeler:
        i = i.strip('\n')
        i = i.strip(' ')
        i = i.strip('.')
        i = i.strip(',')

        self.sade_kelimler.append(i)

      for i in self.sade_kelimler:
        print(i)

  def tum_kelimeler(self):
    kelimeler_kumesi = set()
    for i in self.sade_kelimler:
      kelimeler_kumesi.add(i)

    print('Tum kelimeler..........')
    for i in kelimeler_kumesi:
      print(i)
      print('***********')

  def kelime_frekansi(self):
    kelime_sozluk = dict()
    for i in self.sade_kelimler:
      if i in kelime_sozluk:
        kelime_sozluk[i] += 1
      else:
        kelime_sozluk[i] = 1

    for kelime,sayi in kelime_sozluk.items():
      print('{} kelimesi {} defa geciyor'.format(kelime, sayi))
      print('----------------------')

dosya = Dosya()
dosya.tum_kelimeler()
dosya.kelime_frekansi()