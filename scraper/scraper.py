
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

    def _setup_process(self):
        now = datetime.datetime.now(self.settings.timezone)
        self.process = CrawlerProcess(self._crawler_options(now))
        for site in self.sites:
            self.process.crawl(Spider, settings=site.settings)

    def _crawler_options(self, now):
        """Return crrawlwer options

        `DOWNLOAD_DELAY` is in seconds, and is such that if
        `RANDOMIZE_DOWNLOAD_DELAY` is set to `True`, then the requests will
        happen between 0.5 * `DOWNLOAD_DELAY` and 1.5 * `DOWNLOAD_DELAY`.
        """
        return {
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_FORMAT': self.settings.results_file_type,
            'FEED_URI': self._file_name(now),
            'RANDOMIZE_DOWNLOAD_DELAY': True,
            'COOKIES_ENABLED': False,
            'DOWNLOAD_DELAY': 2
        }

    def _file_name(self, now):
        return "outputs/%(name)s_{}.{}".format(
            now.strftime(TS_FORMAT), self.settings.results_file_type)
