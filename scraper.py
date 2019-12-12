import scrapy

class BrickSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for bset in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.set'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first()
            }