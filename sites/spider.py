
import scrapy

from utilities.inputs import SearchStringsCSV
from .item import Item


class Spider(scrapy.Spider):

    name = 'flatfooted'
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'LOG_LEVEL': 'WARNING'
    }

    def __init__(self, settings={}, **kwargs):
        self.site_settings = settings
        self.start_urls = self._start_urls()
        super().__init__(**kwargs)

    def parse(self, response):
        for i, selector in enumerate(self.site_settings.first_item_selectors):
            first_item = response.xpath(selector).extract_first()
            if first_item:
                yield response.follow(first_item, self._parse_item)
                break

    def _parse_item(self, response):
        yield Item(response, self.site_settings).data()

    def _start_urls(self):
        return [
            self.site_settings.search_query.format(s)
            for s in self._search_strings()
        ]

    def _search_strings(self):
        # To test specific search strings, put them here:
        # return ["3 IN ONE 120039", "3M 2.00E 97", "3M 02554",]
        return SearchStringsCSV(self.site_settings).search_strings()
