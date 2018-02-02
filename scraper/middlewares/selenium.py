
import os

from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):

    def __init__(self):
        #
        # To avoid crashes, I'm using the `driver` as a singleton
        # by putting it into the `__init__()` method instead of
        # restarting it everytime within the `process_request()`
        # method. However, I need to be careful that multiple
        # requests don't try to use the same `driver` due to the
        # concurrency of Scrapy, specifically Twisted.
        #
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self.driver = webdriver.Chrome(
            '{}/../../utilities/chromedriver'.format(
                os.path.dirname(os.path.realpath(__file__))),
            chrome_options=options)
        self.driver.set_page_load_timeout(3)
        self.driver.implicitly_wait(2)

    def __del__(self):
        self.driver.close()

    def process_request(self, request, spider):
        if spider.use_selenium():
            try:
                self.driver.get(request.url)
            except TimeoutException:
                pass
            #
            # TODO: Specify through settings file?
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
            try:
                return HtmlResponse(
                    self.driver.current_url,
                    body=self.driver.page_source,
                    encoding='UTF-8',
                    request=request
                )
            except TimeoutException:
                return None
