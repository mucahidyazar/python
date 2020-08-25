print("""
  QUESTION:
  "şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

      Memlekete sis çökmüş bir gece 
      Usulca yanağıma sen düşüyorsun
      Sabah saat dokuzu beş geçe
      Terk edip bizleri gidiyorsun
      Ayrılık bu kadar yakmamıştı içimizi
      Farkında mısın bilmiyorum
      Aldın beraberinde cumhuriyetimizi
      Korkunç bir veda, sararmıştı her yer
      Ellerini uzat tutmak istiyoruz
      Masmavi gözleri kaybetmiş çocuk
      Aldı bir sabah ruhumuzu
      Lakin nasıl bölmesin yokluğun uykumuzu

  Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.
""")

with open('siir.txt', 'r', encoding='utf-8') as siir:
  siirLines = siir.readlines()
  newString = ''
  for x in siirLines:
    newString += x[0]
  print(newString)
