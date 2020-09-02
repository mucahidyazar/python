import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" #name onemli, unique olmali, cmd den cagrilacak
    quote_count = 1
    file = open('quotes.txt', 'a', encoding='utf-8')
    start_urls = [
      'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
      #!TXT DOSYASINA YAZDIRMAK ICIN
      for quote in response.css('div.quote'):
        title = quote.css('span.text::text').extract()[0]
        author = quote.css('small.author::text').extract()[0]
        tags = quote.css('div.tags a.tag::text').extract()

        self.file.write(str(self.quote_count) + '. Quote ----->\n')
        self.file.write('Quote : ' + title + '\n')
        self.file.write('Author : ' + author + '\n')
        self.file.write('Tags : ' + str(author) + '\n')
        self.quote_count += 1

      next_url = response.css('li.next a::attr(href)').extract()[0]
      if next_url is not None:
        next_url = 'http://quotes.toscrape.com'+next_url
        yield  scrapy.Request(url=next_url, callback=self.parse)
      else:
        self.file.close()