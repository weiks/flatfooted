
import random
import pandas


class SearchStringsCSV:

    def __init__(self, settings):
        self.settings = settings

    def search_strings(self):
        s = self.settings
        data = pandas.read_csv(s.search_file)
        avoid = data[s.avoid_on].str.contains(s.name, na=False)
        use = data[s.use_on].str.contains(s.name, na=False)
        all = data[s.use_on].str.contains('ALL', na=False)
        strings = list(data[s.search_string][(use | all) & ~avoid])
        sample = s.search_sample
        if sample:
            strings = random.sample(strings, sample)
        return strings
