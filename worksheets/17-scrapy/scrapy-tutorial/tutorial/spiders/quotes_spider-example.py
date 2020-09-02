import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" #name onemli, unique olmali, cmd den cagrilacak

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ] #2 tane web sitesine gidecegimizi soylutor
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


#title alaini alir request yapilan yerdeki
#response.css('title').extract() #* ['<title>Quotes to Scrape</title>']
#response.xpath('//title') #* ['<title>Quotes to Scrape</title>']

#response.css('title::text').extract() #* ['Quotes to Scrape']
#response.css('title::text').extract()[0] #*'Quotes to Scrape'
#response.css('title::text').extract_first() #*'Quotes to Scrape'
#response.xpath('//title/text').extract_first() #*'Quotes to Scrape'


















