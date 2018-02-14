
import random

from .constants import PROXIES


class ProxiesMiddleware:

    def __init__(self):
        self.proxies = PredefinedProxies().list()

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxies)


class PredefinedProxies:

    def __init__(self):
        self.proxies = PROXIES

    def list(self):
        return self.proxies
