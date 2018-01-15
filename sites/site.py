
import pytz
import datetime

from scrapy.crawler import CrawlerProcess

from utilities.constants import TS_FORMAT
from .spider import Spider


class Site:

    file_type = 'csv'

    def __init__(self, name, settings):
        self.name = name
        self.settings = settings
        self._check_required_fields()

    def scrape(self, async=False):
        if async:
            return self._scrape
        self._scrape()

    def _scrape(self):
        now = datetime.datetime.now(pytz.timezone(self.settings['timezone']))
        print("[+] {} @ {}...".format(self.name, now.strftime(TS_FORMAT)))
        process = CrawlerProcess(self._crawler_options(now))
        process.crawl(Spider, name=self.name, settings=self.settings)
        process.start()

    def _crawler_options(self, now):
        return {
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_URI': self._file_name(now),
            'FEED_FORMAT': self.file_type
        }

    def _file_name(self, now):
        return "outputs/{}_{}.csv".format(self.name, now.strftime(TS_FORMAT))

    def _check_required_fields(self):
        site_fields = self.settings[self.name]['fields']
        site_fields_keys = list(site_fields.keys())
        for field in self.settings['required_fields']:
            if field not in site_fields_keys or not site_fields[field]:
                raise ValueError("Missing required field ({})".format(field))
