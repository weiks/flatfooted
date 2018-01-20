
import random
import pprint

from proxies.proxies import PredefinedProxies
# from proxies.proxies import RealTimeProxies

from .constants import USER_AGENTS


class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(USER_AGENTS))


class ProxyMiddleware:

    def __init__(self):
        # self.proxies = RealTimeProxies().list()
        self.proxies = PredefinedProxies().list()

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxies)
        print('-' * 50)
        pprint.pprint(request.__dict__)
        print('-' * 50)
