
import random

from .constants import USER_AGENTS, PROXIES


class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(USER_AGENTS))


class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(PROXIES)
        #
        # To check that effectively each request is being issued with a
        # different proxy and user-agent header, uncomment the following:
        #
        from pprint import pprint
        print('1' * 50)
        pprint(request.__dict__)
        print('1' * 50)
