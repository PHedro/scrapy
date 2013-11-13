__author__ = 'phedro'
from scrapy.spider import BaseSpider
from scrapy.http.request import Request


class SSpider3(BaseSpider):
    name = "sspider3"
    allowed_domains = ["hughes.sieve.com.br"]
    start_urls = ["http://hughes.sieve.com.br:8000/level31/"]

    def parse(self, response):
        filename = 'level3.txt'
        pattern_to_find = "R$ "
        prices = 'None'
        if pattern_to_find in response.body:
            splitted = response.body.split(pattern_to_find)
            splitted.pop(0)
            prices = ''
            for piece in splitted:
                piece = piece[:piece.index(',')+3]
                prices += '{0} {1}; '.format(
                    pattern_to_find, piece.split(" ")[0]
                )

        open(filename, 'wb').write(prices)
        return Request(
            url="http://hughes.sieve.com.br:8000/level3/",
            cookies={
                'name': '18',
                'value': '',
                'domain': 'hughes.sieve.com.br',
                'expires': 'session',
                'path': '/'
            },
        )