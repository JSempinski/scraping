import scrapy


class YesspiderSpider(scrapy.Spider):
    name = "yesspider"

    def start_request(self):
        yield scrapy.Request('https://yes.pl/',
        meta={'playwright': True})


    def parse(self, response):
        yield {
            'text': response.text
        }
