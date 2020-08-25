print("""
  QUESTION:
  Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

      coskun.m.murat@gmail.com
      example@xyz.com
      mustafa.com
      mustafa@gmail
      kerim@yahoo.com
""")

with open('mailler.txt', 'r', encoding='utf-8') as mailler:
  mailLines = mailler.readlines()
  for x in mailLines:
    if '@' in x and '.com' in x:
      print(x[:-1], '✅')
    else:
      print(x[:-1], '❌')