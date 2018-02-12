
import json
import pandas

from pprint import pprint

data = json.load(open('skus.json'))

pprint(data)

clean_data = []

for page in data:
    for link in page['links']:
        clean_data.append([
            page['timestamp'],
            page['page'],
            page['heading'],
            link['sku'],
            link['url']
        ])

columns = ['timestamp', 'page', 'heading', 'sku', 'url']
df = pandas.DataFrame(clean_data, columns=columns)
df.to_csv('./skus.csv', index=False)
