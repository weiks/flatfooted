
import os

from scrapy.exceptions import IgnoreRequest

from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        driver = SeleniumDriver().driver
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
        try:
            driver.find_element_by_class_name('PageNm')
        except:
            pass


class SeleniumDriver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self._driver = webdriver.Chrome(
            '{}/../../../../../utilities/chromedriver'.format(
                os.path.dirname(os.path.realpath(__file__))),
            chrome_options=options)
        self._driver.set_page_load_timeout(90)
        self._driver.implicitly_wait(60)

    @property
    def driver(self):
        return self._driver
