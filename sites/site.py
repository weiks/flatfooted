
import datetime

from scrapy.crawler import CrawlerProcess

from utilities.constants import TS_FORMAT
from utilities.settings import Settings
from .spider import Spider


class Site:

    def __init__(self, name, settings):
        self.settings = Settings(name, settings)
        self._check_required_fields()

    def scrape(self, async=False):
        if async:
            return self._scrape
        self._scrape()

    def _scrape(self):
        now = datetime.datetime.now(self.settings.timezone)
        process = CrawlerProcess(self._crawler_options(now))
        process.crawl(Spider, settings=self.settings)
        process.start()

    def _crawler_options(self, now):
        return {
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_FORMAT': self.settings.results_file_type,
            'FEED_URI': self._file_name(now)
        }

    def _file_name(self, now):
        return "outputs/{}_{}.{}".format(
            self.settings.name,
            now.strftime(TS_FORMAT),
            self.settings.results_file_type
        )

    def _check_required_fields(self):
        for field in self.settings.required_fields:
            if field not in self.settings.field_keys:
                raise ValueError("Missing required field ({})".format(field))
            if not self.settings.fields[field]:
                raise ValueError("Invalid required field ({})".format(field))
