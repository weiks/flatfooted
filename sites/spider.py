
import scrapy

from utilities.inputs import SearchStringsCSV
from .item import Item


class Spider(scrapy.Spider):

    name = 'flatfooted'
    custom_settings = {'AUTOTHROTTLE_ENABLED': True}

    def __init__(self, name='', settings={}, **kwargs):
        self.site_name = name
        self.site_settings = settings
        self.start_urls = self._start_urls()
        self.first_item_selector = (
            settings[name]['search']['first_item'])
        self.first_item_fallback_selector = (
            settings[name]['search']['first_item_fallback'])
        super().__init__(**kwargs)

    def parse(self, response):
        first_item = response.xpath(
            self.first_item_selector).extract_first()
        first_item_fallback = response.xpath(
            self.first_item_fallback_selector).extract_first()
        if first_item:
            yield response.follow(first_item, self._parse_item)
        elif first_item_fallback:
            yield response.follow(first_item_fallback, self._parse_item)

    def _parse_item(self, response):
        yield Item(response, self.site_name, self.site_settings).data()

    def _start_urls(self):
        query = self.site_settings[self.site_name]['search']['query']
        return [query.format(s) for s in self._search_strings()]

    def _search_strings(self):
        # To test specific search strings, put them here:
        # return ["3 IN ONE 120039", "3M 2.00E 97", "3M 02554",]
        return SearchStringsCSV(self.site_settings).search_strings()
