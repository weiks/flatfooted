
from argparse import ArgumentParser
from pymongo import MongoClient
from pandas import DataFrame

DB_NAME = 'flatfooted'
DB_HOST = 'localhost'
DB_PORT = 27017

DB = MongoClient(DB_HOST, DB_PORT)
SEARCHES = DB[DB_NAME]['searches']
ITEMS = DB[DB_NAME]['items']

parser = ArgumentParser()
parser.add_argument("--date-start", help="Format: YYYY-MM-DD-hh-mm")
parser.add_argument("--date-end", help="Format: YYYY-MM-DD-hh-mm")
parser.add_argument("--site", help="As found in `settings.py`")
parser.add_argument("--sku", help="As found in `site_id` column")
args = parser.parse_args()


def db_to_csv(date_start=None, date_end=None, sku=None, site=None):
    check_arguments(date_start, date_end, sku, site)
    i_query = items_query(date_start, date_end, sku, site)
    items_cursor = ITEMS.find(i_query)
    items = DataFrame.from_records(items_cursor)
    items.to_csv("./items.csv", index=False)


def items_query(date_start, date_end, sku, site):
    query = {}
    if date_start and date_end:
        query['timestamp'] = {"$lt": date_end, "$gt": date_start}
    if sku:
        query['site_id'] = {"$regex": ".*{}.*".format(sku)}
    if site:
        query['site_name'] = site
    return query


def searches_query(items, date_start, date_end, sku, site):
    pass


def check_arguments(date_start, date_end, sku, site):
    if date_start is not None and date_end is not None:
        check_date(date_start)
        check_date(date_end)
        date_range = True
    else:
        date_range = False
    if not date_range and not sku and not site:
        raise ValueError("Specify one dimension to query for (see --help)")


def check_date(string):
    if False:
        raise ValueError("Date format error: YYYY-MM-DD-hh-mm")


# Run automatically after functions have been loaded
db_to_csv(args.date_start, args.date_end, args.sku, args.site)
