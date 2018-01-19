
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
        super().__init__(**kwargs)

    def start_requests(self):
        for combination in self._start_combinations():
            search_string = combination['search_string']
            yield scrapy.Request(
                combination['url'],
                callback=self._parse_searches_wrapper(search_string),
                errback=self._parse_search_error_wrapper(search_string)
            )

    def _parse_searches_wrapper(self, search_string):
        def _parse_searches(self, response):
            selectors = self.site_settings.first_item_selectors
            key = self.site_settings.first_item_selectors_key
            returned_results = False
            for i, selector in enumerate(selectors):
                first_item = select(response, key, selector).extract_first()
                if first_item:
                    returned_results = True
                    yield response.follow(
                        first_item,
                        callback=self._parse_item_wrapper(search_string),
                        errback=self._parse_item_error_wrapper(search_string)
                    )
                    break
            yield self._parse_search(response, returned_results, search_string)
        return _parse_searches

    def _parse_item_wrapper(self, search_string):
        def _parse_item(self, response):
            yield Item(
                response,
                self.site_settings,
                search_string
            ).data()
        return _parse_item

    def _parse_item_error_wraper(self, search_string):
        def _parse_item_error(self, response):
            yield Item(
                response,
                self.site_settings,
                search_string,
                error=True
            ).data()
        return _parse_item_error

    def _parse_search(self, response, returned_results, search_string):
        return Search(
            response,
            self.site_settings,
            returned_results,
            search_string
        ).data()

    def _parse_search_error_wrapper(self, search_string):
        def _parse_search_error(self, response):
            return Search(
                response,
                self.site_settings,
                returned_results=None,
                search_string=search_string,
                error=True
            ).data()
        return _parse_search_error

    def _start_combinations(self):
        return [
            {
                'url': self.site_settings.search_query.format(search_string),
                'search_string': search_string
            }
            for search_string in self._search_strings()
        ]

    def _search_strings(self):
        return SearchStringsCSV(self.site_settings).search_strings()
