
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from scrapy.exceptions import IgnoreRequest
from pprint import pprint

from utilities.select import select


class Parser:

    url_type = None

    def __init__(self, response, settings, error):
        self.should_parse = False
        self.settings = settings
        self.response = response
        self.error = error
        if error:
            self.url = response.request.url
            if response.check(HttpError):
                self.response_status = 'HTTP Error {}'.format(
                    response.value.response.status)
            elif response.check(DNSLookupError):
                self.response_status = 'DNS Lookup Error'
            elif response.check(TimeoutError, TCPTimedOutError):
                self.response_status = 'TCP Timeout Error'
            elif response.check(IgnoreRequest):
                self.response_status = 'Selenium Timeout Error'
            else:
                self._print_error_info()
                raise ValueError("Is there a missing case for errors?")
        else:
            self.should_parse = True
            self.url = response.url
            self.response_status = 'HTTP {}'.format(self.response.status)

    def data(self):
        data = self._initial_data()
        if self.should_parse:
            for key in self.fields:
                text = ''
                for i, selector in enumerate(self.fields[key]):
                    raw_text = self._raw_text(key, selector)
                    if raw_text:
                        text = raw_text
                        i += 1
                        break
                clean_text = text.encode("ascii", errors="ignore").decode()
                data[key] = clean_text
                data["{}_selector".format(key)] = i
        return data

    def _initial_data(self):
        if hasattr(self.response, 'meta'):
            data = self.response.meta['custom_variables']
        elif hasattr(self.response.value, 'response'):
            data = self.response.value.response.meta['custom_variables']
        else:
            data = {'Error': 'No metadata in response?'}
            self._print_error_info()
            print('!' * 100)
            print("Is there a missing case for metadata?")
            print('!' * 100)
        data[self.response_status_variable] = self.response_status
        data[self.url_variable] = self.url
        return data

    def _raw_text(self, key, selector):
        texts_list = select(self.response, key, selector).extract()
        return ' '.join(' '.join(texts_list).split()) if texts_list else []

    def _print_error_info(self):
        print('!' * 100)
        print('Should parse:')
        print(self.should_parse)
        print('Response:')
        pprint(self.response.__dict__)
        print('Error:')
        print(self.error)
        print('URL:')
        print(self.url)
        print('!' * 100)


class Item(Parser):

    def __init__(self, response, settings, error=False):
        self.url_variable = 'url_item'
        self.response_status_variable = 'response_status_item'
        self.fields = settings.item_fields
        super().__init__(response, settings, error)


class Search(Parser):

    def __init__(self, response, settings, returned_results=None, error=False):
        self.url_variable = 'url_search'
        self.response_status_variable = 'response_status_search'
        self.returned_results = returned_results
        self.fields = settings.search_fields
        super().__init__(response, settings, error)
