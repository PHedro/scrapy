__author__ = 'phedro'
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.http.response import Response


class SSpider(BaseSpider):
    name = "sspider2"
    allowed_domains = ["hughes.sieve.com.br"]
    start_urls = ["http://hughes.sieve.com.br:8000/level2/"]

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
        return Request(
            url=response.url,
            cookies={
                'name': 'd53db4de415c4e858dc761595623a898',
                'value': '',
                'domain': 'hughes.sieve.com.br',
                'expires': 'session',
                'path': '/'
            },
        )
