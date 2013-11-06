__author__ = 'phedro'
from scrapy.spider import BaseSpider


class SSpider(BaseSpider):
    name = "sspider"
    allowed_domains = ["hughes.sieve.com.br"]
    start_urls = [
        "http://hughes.sieve.com.br:8000/level1/",
        "http://hughes.sieve.com.br:8000/level2/",
        "http://hughes.sieve.com.br:8000/level3/",
        "http://hughes.sieve.com.br:8000/level4/",
        "http://hughes.sieve.com.br:8000/level5%25/"
    ]

    def parse(self, response):
        filename = '{0}.txt'.format(response.url.split("/")[-2])
        pattern_to_find = "R$ "
        prices = 'None'
        if pattern_to_find in response.body:
            splitted = response.body.split(pattern_to_find)
            splitted.pop(0)
            prices = ''
            for piece in splitted:
                prices += '{0} {1}; '.format(
                    pattern_to_find, piece.split(" ")[0]
                )

        open(filename, 'wb').write(prices)
