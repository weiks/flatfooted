
import os

from scrapy.exceptions import IgnoreRequest

from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        if spider.use_selenium():
            driver = SeleniumDriver(request.meta.get('proxy', None)).driver
            try:
                driver.get(request.url)
            except TimeoutException:
                raise IgnoreRequest()
            self._wait_for_page(driver, spider, request)
            return HtmlResponse(
                driver.current_url,
                body=driver.page_source,
                encoding='UTF-8',
                request=request
            )

    def _wait_for_page(self, driver, spider, request):
            #
            # Make Selenium wait for a pre-specified selector
            # TODO: Specify these cases through settings file?
            #
            if spider.name == 'CDW' and request.meta['type'] == 'search':
                try:
                    driver.find_element_by_class_name('search-results-for')
                except:
                    pass
            if spider.name == 'NSIT' and request.meta['type'] == 'search':
                try:
                    driver.find_element_by_css_selector('#buy-counter')
                    driver.find_element_by_css_selector('.select-prod')
                except:
                    pass
            if spider.name == 'NSIT' and request.meta['type'] == 'item':
                try:
                    driver.find_element_by_css_selector('.prod-price')
                except:
                    pass
            if spider.name == 'STAPLES' and request.meta['type'] == 'search':
                try:
                    driver.find_element_by_css_selector(
                        'body > div.stp--container-sm.no-results > h1')
                except:
                    pass
            if spider.name == 'ESND' and request.meta['type'] == 'search':
                try:
                    driver.find_element_by_css_selector(
                        'div.ess-product-desc')
                except:
                    pass
            if spider.name == 'ESND' and request.meta['type'] == 'item':
                try:
                    driver.find_element_by_css_selector(
                        'div.ess-product-price')
                except:
                    pass
            if spider.name == 'ZORO' and request.meta['type'] == 'search':
                try:
                    driver.find_element_by_css_selector(
                        '#grid > li:nth-child(1) > div')
                except:
                    pass
            if spider.name == 'ZORO' and request.meta['type'] == 'item':
                try:
                    driver.find_element_by_css_selector(
                        '#avl-info-icon > span > i')
                except:
                    pass


class SeleniumDriver:

    def __init__(self, proxy=None):
        options = webdriver.ChromeOptions()
        if proxy:
            print('-' * 100)
            print('Selenium using proxy: {}'.format(proxy))
            print('-' * 100)
            options.add_argument('--proxy-server={}'.format(proxy))
        options.add_argument('headless')
        self._driver = webdriver.Chrome(
            '{}/../../../utilities/chromedriver'.format(
                os.path.dirname(os.path.realpath(__file__))),
            chrome_options=options)
        self._driver.set_page_load_timeout(30)
        self._driver.implicitly_wait(15)

    @property
    def driver(self):
        return self._driver
