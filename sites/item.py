
class Item:

    def __init__(self, response, name, settings):
        self.name = name
        self.settings = settings
        self.response = response

    def data(self):
        fields = self.settings[self.name]['fields']
        data = {'url': self.response.url}
        for key in fields.keys():
            if 'fallback' not in key:
                raw_text = self.response.xpath(
                    fields[key]).extract_first()
                key_fallback = fields.get('{}_fallback'.format(key), None)
                if key_fallback:
                    raw_text_fallback = self.response.xpath(
                        key_fallback).extract_first()
                else:
                    raw_text_fallback = None
                if raw_text:
                    clean_text = raw_text.strip()
                elif raw_text_fallback:
                    clean_text = raw_text_fallback.strip()
                else:
                    clean_text = ''
                data[key] = clean_text
        return data
