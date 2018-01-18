
import pandas
import scrapy

from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError

from utilities.inputs import SearchStringsCSV
from utilities.select import select
from .item import Item


class Spider(scrapy.Spider):

    custom_settings = {
        'AUTOTHROTTLE_ENABLED': False,
        'LOG_LEVEL': 'DEBUG'
    }

    def __init__(self, settings={}, **kwargs):
        self.failed_urls = []
        self.name = settings.name
        self.site_settings = settings
        self.start_urls = self._start_urls()
        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                errback=self._handle_error,
                dont_filter=True
            )

    def parse(self, response):
        key = self.site_settings.first_item_selectors_key
        for i, selector in enumerate(self.site_settings.first_item_selectors):
            first_item = select(response, key, selector).extract_first()
            if first_item:
                yield response.follow(first_item, self._parse_item)
                break

    def handle_spider_closed(self, spider, reason):
        print('!' * 50)
        print(self.failed_urls)
        print('!' * 50)
        # TODO: Move into it's own class
        data = pandas.DataFrame(self.failed_urls)
        f = "outputs/{}_{}_errors.{}".format(self.name, "0000-00-00", "csv")
        data.to_csv(f, columns=["url", "error"])

    def _parse_item(self, response):
        yield Item(response, self.site_settings).data()

    def _start_urls(self):
        return [
            self.site_settings.search_query.format(s)
            for s in self._search_strings()
        ]

    def _search_strings(self):
        return SearchStringsCSV(self.site_settings).search_strings()

    def _handle_error(self, response):
        print('*' * 50)
        self.logger.error(repr(response))
        if response.check(HttpError):
            error = 'HTTP Error {}'.format(response.status)
        elif response.check(DNSLookupError):
            error = 'DNS Lookup Error'
        elif response.check(TimeoutError, TCPTimedOutError):
            error = 'TCP Timeout Error'
        self.failed_urls.append([response.url, error])
        self.logger.error(error)
        print('*' * 50)
