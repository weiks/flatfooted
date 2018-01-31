
import scrapy

from slugify import slugify

from utilities.inputs import SearchStringsCSV
from utilities.select import select
from .parsers import Item, Search


class Spider(scrapy.Spider):

    custom_settings = {
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.5,
        'AUTOTHROTTLE_ENABLED': True,
        'CONCURRENT_REQUESTS': 16,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'DOWNLOAD_DELAY': 2
    }

    def __init__(self, settings={}, now=None, **kwargs):
        self.now = now
        self.name = settings.name
        self.site_settings = settings
        super().__init__(**kwargs)

    def start_requests(self):
        for combination in self._start_combinations():
            yield scrapy.Request(
                combination['url'],
                callback=self._parse_searches,
                errback=self._parse_search_error,
                meta=self._meta('search', combination['search_string'])
            )

    def _parse_searches(self, response):
        selectors = self.site_settings.first_item_selectors
        key = self.site_settings.first_item_selectors_key
        returned_results = False
        for i, selector in enumerate(selectors):
            first_item = select(response, key, selector).extract_first()
            if first_item:
                returned_results = True
                previous_meta = response.meta['custom_variables']
                yield scrapy.Request(
                    self._enforce_absolute_url(first_item),
                    callback=self._parse_item,
                    errback=self._parse_item_error,
                    meta=self._meta('item', previous_meta['search_string'])
                )
                break
        response.meta['custom_variables'].update({
            'returned_results': returned_results
        })
        yield self._parse_search(response)

    def _enforce_absolute_url(self, url):
        """Enforce URL in possibly relative `url`

        Currently it only checks for HTTP/S protocols at the beginning of the
        URL, but we can possibly find more complex cases as we move along.
        """
        if 'http' not in url and 'https' not in url:
            url = '{}{}'.format(self.site_settings.base_url, url)
        return url

    def _parse_item(self, response):
        self._save_html(response, '_item')
        yield Item(response, self.site_settings,).data()

    def _parse_item_error(self, response):
        self._save_html(response, '_item')
        yield Item(response, self.site_settings, error=True).data()

    def _parse_search(self, response):
        self._save_html(response, '_search')
        return Search(response, self.site_settings).data()

    def _parse_search_error(self, response):
        self._save_html(response, '_search')
        return Search(response, self.site_settings, error=True).data()

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

    def _save_html(self, response, suffix=''):
        if self.site_settings.save_html and hasattr(response, "body"):
            s = response.meta['custom_variables'].get('search_string', False)
            with open(self._file_name('html', s + suffix), 'w+b') as f:
                f.write(response.body)

    def _file_name(self, extension, search_string=None):
        if search_string:
            return 'outputs/html/{}_{}_{}.{}'.format(
                self.name, self.now, slugify(search_string), extension)
        return 'outputs/{}/{}_{}.{}'.format(
            self.name, self.now, extension)

    def _meta(self, request_type, search_string):
        return {
            'type': request_type,
            'site_name': self.name,
            'site_settings': self.site_settings,
            'custom_variables': {
                'search_string': search_string,
                'site_name': self.name,
                'timestamp': self.now
            }
        }

    def use_selenium(self):
        return self.site_settings.javascript
