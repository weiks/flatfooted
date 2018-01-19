
from utilities.select import select

from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError


class Parser:

    url_type = None

    def __init__(self, response, settings, error):
        self.settings = settings
        self.response = response
        self.should_parse = False
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
            else:
                raise ValueError("Is there a missing case?")
        else:
            self.url = response.url
            self.response_status = 'HTTP {}'.format(
                self.response.status)
            self.should_parse = True

    def _initial_data(self):
        return {
            'url': self.url,
            'url_type': self.url_type,
            'response_status': self.response_status
        }

    def data(self):
        raise ValueError("Method must be defined by subclass")

    def _raw_text(self, key, selector):
        texts_list = select(self.response, key, selector).extract()
        return ' '.join(' '.join(texts_list).split()) if texts_list else []


class Item(Parser):

    def __init__(self, response, settings, error=False):
        self.url_type = 'Item'
        super().__init__(response, settings, error)

    def data(self):
        data = self._initial_data()
        if self.should_parse:
            for key in self.settings.fields.keys():
                clean_text = ''
                for i, selector in enumerate(self.settings.fields[key]):
                    raw_text = self._raw_text(key, selector)
                    if raw_text:
                        clean_text = raw_text
                        i += 1
                        break
                data[key] = clean_text
                data["{}_selector".format(key)] = i
        if self.error:
            print('!' * 100)
            from pprint import pprint
            pprint(data)
            print('!' * 100)
        return data


class Search(Parser):

    def __init__(self, response, settings, returned_results, error=False):
        self.url_type = 'Search'
        self.returned_results = returned_results
        super().__init__(response, settings, error)

    def data(self):
        data = self._initial_data()
        data['search_returned_results'] = self.returned_results
        return data
