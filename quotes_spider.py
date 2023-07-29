import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        useragent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
        urls = ['https://www.kurdistan24.net/en/kurdistannews']
        for url in urls:
            yield scrapy.Request(url=url, USER_AGENT = useragent, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb.txt') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)