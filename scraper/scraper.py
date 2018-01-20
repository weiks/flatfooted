
import pandas
import datetime

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

    def json_to_csv(self):
        for name in self.settings.names:
            csv_name = self._file_with_name(name, self.now, 'csv')
            json_name = self._file_with_name(name, self.now)
            results = pandas.read_json(json_name)
            results.to_csv(csv_name, index=False)

    def _setup_process(self):
        self.now = datetime.datetime.now(self.settings.timezone)
        self.process = CrawlerProcess(self._crawler_options(self.now))
        for site in self.sites:
            self.process.crawl(Spider, settings=site.settings)

    def _crawler_options(self, now):
        """Return crrawlwer options

        `DOWNLOAD_DELAY` is in seconds, and is such that if
        `RANDOMIZE_DOWNLOAD_DELAY` is set to `True`, then the requests will
        happen between 0.5 * `DOWNLOAD_DELAY` and 1.5 * `DOWNLOAD_DELAY`.

        `RETRY_TIMES` and `RETRY_HTTP_CODES` must be much more flexible if
        proxies are being used because proxies can fail for a variety of
        reasons, and we need to be able to adapt to that.

        NOTE: Using proxies slows the process quite a bit.
        """
        m = 'DOWNLOADER_MIDDLEWARES'
        options = {
            'FEED_FORMAT': self.settings.results_file_type,
            'FEED_URI': self._file_name(now),
            'COOKIES_ENABLED': False,
            m: {}
        }
        if self.settings.random_proxies:
            options['RETRY_TIMES'] = 10
            options['RETRY_HTTP_CODES'] = [500, 503, 504, 400, 403, 404, 408]
            options[m]['scraper.middleware.ProxyMiddleware'] = 410
        if self.settings.random_user_agents:
            options[m]['scraper.middleware.RandomUserAgentMiddleware'] = 400
        return options

    def _file_with_name(self, name, now, ext=None):
        return self._file_name(now, ext).replace("%(name)s", name)

    def _file_name(self, now, ext=None):
        if ext is None:
            ext = self.settings.results_file_type
        return "outputs/%(name)s_{}.{}".format(now.strftime(TS_FORMAT), ext)
