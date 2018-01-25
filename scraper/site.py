
from utilities.settings import Settings


class Site:

    def __init__(self, name, settings):
        self._settings = Settings(settings, name)
        self._check_required_fields()

    @property
    def settings(self):
        return self._settings

    def _check_required_fields(self):
        for field in self.settings.required_fields:
            if field not in self.settings.item_field_keys:
                raise ValueError("Missing required field ({})".format(field))
            if not self.settings.item_fields[field]:
                raise ValueError("Invalid required field ({})".format(field))
