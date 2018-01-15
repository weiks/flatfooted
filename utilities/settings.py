
import pytz


class Settings:

    def __init__(self, name, settings):
        self.settings = settings
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def timezone(self):
        return pytz.timezone(self.settings['timezone'])

    @property
    def fields(self):
        return self.settings['sites'][self.name]['fields']

    @property
    def field_keys(self):
        return list(self.settings['sites'][self.name]['fields'].keys())

    @property
    def required_fields(self):
        return self.settings['required_fields']

    @property
    def first_item_selectors(self):
        return self.settings['sites'][self.name]['search']['first_item']

    @property
    def search_query(self):
        return self.settings['sites'][self.name]['search']['query']

    @property
    def search_file(self):
        return self.settings['search_strings']['file']

    @property
    def search_variable(self):
        return self.settings['search_strings']['variable']

    @property
    def search_sample(self):
        return self.settings['search_strings']['sample']

    @property
    def results_file_type(self):
        return self.settings['results_file_type']
