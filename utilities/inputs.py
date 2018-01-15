
import random
import pandas


class SearchStringsCSV:

    def __init__(self, settings):
        self.settings = settings

    def search_strings(self):
        data = pandas.read_csv(self.settings.search_file)
        strings = list(data[self.settings.search_variable])
        sample = self.settings.search_sample
        if sample:
            strings = random.sample(strings, sample)
        return strings
