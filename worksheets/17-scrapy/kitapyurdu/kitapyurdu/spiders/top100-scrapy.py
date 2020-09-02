import scrapy

class topScrapy(scrapy.Spider):
  name = 'top'
  book_count = 1
  file = open('books.txt', 'a', encoding='utf-8')
  start_urls = [ 'https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html' ]

  def parse(self, response):
    for book in response.xpath('/html/body/div[3]/div/div[3]/div/div[1]/div[2]/div'):
      name = book.css('.name a span::text').extract()[0]
      author = book.css('.author span a span::text').extract()[0]
      publisher = book.css('.publisher span a span::text').extract()[0]
      self.file.write("""
        BOOK {}
        name: {}
        author: {}
        publisher: {}
      """.format(self.book_count, name, author, publisher))
      self.book_count += 1

    next_url = response.css('.pagination .links .next::attr(href)').extract()[0]
    if next_url is not None:
      yield scrapy.Request(url=next_url, callback=self.parse)
    else: self.file.close()

    