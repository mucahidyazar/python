class Yazilimci():
  def __init__(self, isim, soyisim, numara, maas, diller):
    self.isim = isim
    self.soyisim = soyisim
    self.numara = numara
    self.maas = maas
    self.diller = diller

  #KENDI METHODLARIMIZ
  #Method tanitirken objemize erismek icin her zaman ilk argument olarak selfi yazmamiz gerekiyor
  def bilgileriGoster(self):
    print("""
      Yazilimci objesinin ozellikleri
      Isim : {}
      Soyisim: {}
      Numara: {}
      Maas: {}
      Diller: {}
    """.format(self.isim, self.soyisim, self.numara, self.maas, self.diller))

  def zamYap(self, zamMiktari):
    print('Zam yapiliyor...')
    self.maas += zamMiktari

  def dilEkle(self, yeniDil):
    print('Dil ekleniyor')
    self.diller.append(yeniDil)

yazilimci1 = Yazilimci('Mustafa Murat', 'Coskun', 12345, 3000, ['Python', 'Java', 'C', 'Javascript'])
yazilimci1.bilgileriGoster()
yazilimci1.zamYap(500)
yazilimci1.dilEkle('GoLang')
yazilimci1.bilgileriGoster()