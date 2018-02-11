
import settings_site as s

SETTINGS = {
    'save_html': True,
    'random_proxies': True,
    'random_user_agents': True,
    'timezone': 'America/Mexico_City',
    'search_strings': {
        'file': 'inputs/search-strings-full.csv',
        'search_string': 'SearchString',
        'avoid_on': 'AvoidOn',
        'use_on': 'UseOn',
        'sample': 50
    },
    'mongo': {
        'db': 'flatfooted',
        'host': 'localhost',
        'port': 27017
    },
    'required_fields': [
        'name',
        'price'
    ],
    'sites': {
        #
        # Standard
        #
        'AMZN': s.AMZN,
        'CDW': s.CDW,
        'FAST': s.FAST,
        'BUNZL': s.BUNZL,
        'PCMI': s.PCMI,
        'HDSS': s.HDSS,
        'CNXN': s.CNXN,
        #
        # JavaScript
        #
        'ZORO': s.ZORO,
        'GWW': s.GWW,
        'NSIT': s.NSIT,
        'STAPLES': s.STAPLES,
        'ESND': s.ESND,
        #
        # Search Page
        #
        'TECD': s.TECD,
        #
        # Double-hops
        #
        'MSM': s.MSM,
        'AZO': s.AZO
    }
}
