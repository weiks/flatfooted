
import scrapy

from utilities.inputs import SearchStringsCSV
from utilities.select import select
from .parsers import Item, Search


class Spider(scrapy.Spider):

    custom_settings = {
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 5,
        'AUTOTHROTTLE_ENABLED': True,
        'LOG_LEVEL': 'DEBUG'
    }

    def __init__(self, settings={}, **kwargs):
        self.name = settings.name
        self.site_settings = settings
        self.start_urls = self._start_urls()
        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self._parse_searches,
                errback=self._parse_search_error
            )

    def _parse_searches(self, response):
        key = self.site_settings.first_item_selectors_key
        returned_results = False
        for i, selector in enumerate(self.site_settings.first_item_selectors):
            first_item = select(response, key, selector).extract_first()
            if first_item:
                returned_results = True
                yield response.follow(
                    first_item,
                    callback=self._parse_item,
                    errback=self._parse_item_error
                )
                break
        yield self._parse_search(response, returned_results)

    def _parse_item(self, response):
        yield Item(response, self.site_settings).data()

    def _parse_search(self, response, returned_results):
        return Search(response, self.site_settings, returned_results).data()

    def _parse_item_error(self, response):
        # self.logger.error(repr(response))
        yield Item(response, self.site_settings, error=True).data()

    def _parse_search_error(self, response):
        # self.logger.error(repr(response))
        return Search(response, self.site_settings, error=True).data()

    def _start_urls(self):
        return [
            self.site_settings.search_query.format(s)
            for s in self._search_strings()
        ]

    def _search_strings(self):
        return SearchStringsCSV(self.site_settings).search_strings()
