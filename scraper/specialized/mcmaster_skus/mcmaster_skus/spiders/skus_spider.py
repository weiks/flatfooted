
import scrapy

from datetime import datetime

BATCH_SIZE = 1000
TS_FORMAT = "%Y-%m-%d-%H-%M"
HEADING = '//*[@id="CtlgPageShell_CtlgPage_Inner"]//h1//text()'
SKUS_PARTNBR_LINKS = '//*//a[@data-mcm-partnbr]/@href'
SKUS_PRICES = '//*//td[contains(@class, "ItmTblCellPrce")]//text()'


class SKUsSpider(scrapy.Spider):

    name = "skus"

    def __init__(self, block=None, **kwargs):
        if block is None:
            raise ValueError("Missing block ($ scrapy ... -a block=1")
        self.block = int(block)
        super().__init__(**kwargs)

    def start_requests(self):
        start = 1 + (self.block - 1) * BATCH_SIZE
        end = self.block * BATCH_SIZE
        if self.block == 1:
            start += 1
        combinations = [
            {'url': 'https://www.mcmaster.com/#{}'.format(i), 'page': i}
            for i in range(start, end)
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
            'heading': response.xpath(HEADING).extract_first(),
            'landing': response.url,
            'links': self._links(response)
        }

    def _links(self, response):
        links = response.xpath(SKUS_PARTNBR_LINKS).extract()
        prices = response.xpath(SKUS_PRICES).extract()
        return [{
            'sku': self._sku(l),
            'url': self._url(l),
            'price_landing': prices[i]
        } for i, l in enumerate(links)]

    def _sku(self, link):
        return link.replace('/#', '')

    def _url(self, link):
        return 'https://www.mcmaster.com{}'.format(link)
