
import pandas

from datetime import datetime
from scrapy.crawler import CrawlerProcess

from utilities.constants import TS_FORMAT
from utilities.settings import Settings

from .spider import Spider
from .site import Site


class Scraper:

    def __init__(self, settings):
        self.settings = Settings(settings)
        self.sites = [Site(name, settings) for name in self.settings.names]
        self._setup_process()

    def start(self):
        self.process.start()
        self._json_to_csv()

    def _json_to_csv(self):
        for name in self.settings.names:
            csv_name = self._file_with_name(name, ext='csv')
            json_name = self._file_with_name(name)
            data = pandas.read_json(json_name)
            results = self._postprocess_dataframe(data)
            results.to_csv(csv_name)

    def _postprocess_dataframe(self, data):
        if 'url_item' in data.columns and 'url_search' in data.columns:
            searches = (
                data[data['url_item'].isnull()]
                .set_index('search_string')
                .dropna(axis='columns', how='all')
            )
            items = (
                data[data['url_search'].isnull()]
                .set_index('search_string')
                .dropna(axis='columns', how='all')
            )
            results = searches.join(items, how='outer', rsuffix='_delete')
            return results[[c for c in results.columns if '_delete' not in c]]
        return data

    def _setup_process(self):
        self.now = datetime.now(self.settings.timezone).strftime(TS_FORMAT)
        self.process = CrawlerProcess(self._crawler_options())
        for site in self.sites:
            self.process.crawl(Spider, settings=site.settings, now=self.now)

    def _crawler_options(self):
        """Return crrawlwer options

        `DOWNLOAD_DELAY` is in seconds, and is such that if
        `RANDOMIZE_DOWNLOAD_DELAY` is set to `True`, then the requests will
        happen between 0.5 * `DOWNLOAD_DELAY` and 1.5 * `DOWNLOAD_DELAY`.

        `RETRY_TIMES` and `RETRY_HTTP_CODES` must be much more flexible if
        proxies are being used because proxies can fail for a variety of
        reasons, and we need to be able to adapt to that.
        """
        options = {
            'FEED_FORMAT': 'json',
            'FEED_URI': self._file_name(),
            'COOKIES_ENABLED': False,
            'LOG_LEVEL': 'DEBUG',
            'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
                'scraper.middlewares.CustomRetriesMiddleware': 550,
                'scraper.middlewares.SeleniumMiddleware': 450
            }
        }
        m = 'DOWNLOADER_MIDDLEWARES'
        if self.settings.random_proxies:
            # options['RETRY_TIMES'] = 3
            # options['RETRY_HTTP_CODES'] = [500, 503, 504, 400, 403, 404, 408]
            # TODO: Test that Selenium also uses these proxies
            options[m]['scraper.middlewares.ProxiesMiddleware'] = 410
        if self.settings.random_user_agents:
            options[m]['scraper.middlewares.RandomUserAgentsMiddleware'] = 400
        if self.settings.mongo:
            options['ITEM_PIPELINES'] = {
                'scraper.pipelines.MongoWriterPipeline': 700
            }
        return options

    def _file_with_name(self, name, ext='json'):
        return self._file_name(ext).replace("%(name)s", name)

    def _file_name(self, ext='json'):
        return "outputs/%(name)s_{}.{}".format(self.now, ext)
