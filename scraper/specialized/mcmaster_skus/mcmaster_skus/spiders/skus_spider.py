
import scrapy

from pprint import pprint
from datetime import datetime

TS_FORMAT = "%Y-%m-%d-%H-%M"
HEADING = '//*[@id="CtlgPageShell_CtlgPage_Inner"]//h1//text()'
SKUS_PARTNBR_LINKS = '//*//a[@data-mcm-partnbr]/@href'


class SKUsSpider(scrapy.Spider):

    name = "skus"

    def start_requests(self):
        combinations = [
            {'url': 'https://www.mcmaster.com/#{}'.format(i), 'page': i}
            for i in range(2, 3940)
        ]
        for c in combinations:
            yield scrapy.Request(
                url=c['url'],
                callback=self.parse,
                meta={'page': c['page']}
            )

    def parse(self, response):
        return {
            'timestamp': datetime.now().strftime(TS_FORMAT),
            'page': response.meta.get('page', None),
            'heading': response.xpath(HEADING).extract_first(),
            'links': self._links(response)
        }

    def _links(self, response):
        links = []
        for item in self._items(response):
            links.append({'sku': item['sku'], 'url': item['url']})
        return links

    def _items(self, response):
        links = response.xpath(SKUS_PARTNBR_LINKS).extract()
        items = [{'sku': self._sku(l), 'url': self._url(l)} for l in links]
        pprint(items)
        return items

    def _sku(self, link):
        return link.replace('/#', '')

    def _url(self, link):
        return 'https://www.mcmaster.com{}'.format(link)
