
import random
import pandas


class SearchStringsCSV:

    def __init__(self, settings):
        self.settings = settings['search_strings']

    def search_strings(self):
        data = pandas.read_csv(self.settings['file'])
        strings = list(data[self.settings['variable']])
        sample = self.settings['sample']
        if sample:
            strings = random.sample(strings, sample)
        return strings
