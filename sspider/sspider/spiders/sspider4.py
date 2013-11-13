__author__ = 'phedro'
from scrapy.spider import BaseSpider
from scrapy.http.request import Request


class SSpider4(BaseSpider):
    name = "sspider4"
    allowed_domains = ["hughes.sieve.com.br"]
    start_urls = ["http://hughes.sieve.com.br:8000/level4/"]

    def parse(self, response):
        filename = 'level4.txt'
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
        return Request(
            url="http://hughes.sieve.com.br:8000/level4/",
            cookies={
                'name': 'cade-meu-cookie',
                'value': 'esta aqui',
                'domain': 'hughes.sieve.com.br',
                'expires': 'session',
                'path': '/'
            },
        )