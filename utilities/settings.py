
import pytz


class Settings:

    def __init__(self, settings, name=None):
        self.settings = settings
        self._name = name

    @property
    def names(self):
        return list(self.settings['sites'].keys())

    @property
    def name(self):
        return self._name

    @property
    def timezone(self):
        return pytz.timezone(self.settings['timezone'])

    @property
    def fields(self):
        return self._site_settings['fields']

    @property
    def field_keys(self):
        return list(self._site_settings['fields'].keys())

    @property
    def required_fields(self):
        return self.settings['required_fields']

    @property
    def first_item_selectors_key(self):
        is_xpath = self._site_settings['search'].get('first_item')
        return 'first_item' if is_xpath else 'first_item_css'

    @property
    def first_item_selectors(self):
        return self._site_settings['search'][self.first_item_selectors_key]

    @property
    def search_query(self):
        return self._site_settings['search']['query']

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

    @property
    def _site_settings(self):
        if not self._name:
            raise ValueError('Global settings instance (without `name`)')
        return self.settings['sites'][self.name]
