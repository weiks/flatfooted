
import random
import pprint

from .constants import USER_AGENTS, PROXIES


class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(USER_AGENTS))


class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(PROXIES)
        print('-' * 50)
        pprint.pprint(request.__dict__)
        print('-' * 50)
