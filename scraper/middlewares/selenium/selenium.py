
import os

from scrapy.exceptions import IgnoreRequest

from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):

    def __init__(self):
        self.driver = None
        self._setup_driver()

    def __del__(self):
        self.driver.close()

    def process_request(self, request, spider):
        self._setup_driver(request.meta.get('proxy', None))
        if spider.use_selenium():
            try:
                self.driver.get(request.url)
            except TimeoutException:
                raise IgnoreRequest()
            #
            # Make Selenium wait for a pre-specified selector
            # TODO: Specify these cases through settings file?
            #
            if spider.name == 'CDW' and request.meta['type'] == 'search':
                try:
                    self.driver.find_element_by_class_name('search-results-for')
                except:
                    pass
            if spider.name == 'NSIT' and request.meta['type'] == 'search':
                try:
                    self.driver.find_element_by_css_selector('#buy-counter')
                    self.driver.find_element_by_css_selector('.select-prod')
                except:
                    pass
            if spider.name == 'NSIT' and request.meta['type'] == 'item':
                try:
                    self.driver.find_element_by_css_selector('.prod-price')
                except:
                    pass
            if spider.name == 'STAPLES' and request.meta['type'] == 'search':
                try:
                    self.driver.find_element_by_css_selector(
                        'body > div.stp--container-sm.no-results > h1')
                except:
                    pass
            if spider.name == 'ESND' and request.meta['type'] == 'search':
                try:
                    self.driver.find_element_by_css_selector(
                        'div.ess-product-desc')
                except:
                    pass
            if spider.name == 'ESND' and request.meta['type'] == 'item':
                try:
                    self.driver.find_element_by_css_selector(
                        'div.ess-product-price')
                except:
                    pass

            return HtmlResponse(
                self.driver.current_url,
                body=self.driver.page_source,
                encoding='UTF-8',
                request=request
            )

    def _setup_driver(self, proxy=None):
        #
        # To avoid crashes, I'm using the `driver` as a singleton
        # by putting it into the `__init__()` method instead of
        # restarting it everytime within the `process_request()`
        # method. However, I need to be careful that multiple
        # requests don't try to use the same `driver` due to the
        # concurrency of Scrapy, specifically Twisted.
        #
        if self.driver:
            self.driver.close()
        options = webdriver.ChromeOptions()
        if proxy:
            options.add_argument('--proxy-server={}'.format(proxy))
        options.add_argument('headless')
        self.driver = webdriver.Chrome(
            '{}/../../../utilities/chromedriver'.format(
                os.path.dirname(os.path.realpath(__file__))),
            chrome_options=options)
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(15)
