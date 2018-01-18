
from utilities.select import select


class Item:

    def __init__(self, response, settings):
        self.settings = settings
        self.response = response

    def data(self):
        data = {'url': self.response.url}
        for key in self.settings.fields.keys():
            clean_text = ''
            for i, selector in enumerate(self.settings.fields[key]):
                raw_text = self._raw_text(key, selector)
                if raw_text:
                    clean_text = raw_text
                    i += 1
                    break
            data[key] = clean_text
            data["{}_selector".format(key)] = i
        return data

    def _raw_text(self, key, selector):
        texts_list = select(self.response, key, selector).extract()
        return ' '.join(' '.join(texts_list).split()) if texts_list else []
