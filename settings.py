
SETTINGS = {
    'timezone': 'America/Mexico_City',
    'search_strings': {
        'file': 'inputs/search-strings.csv',
        'variable': 'String',
        'sample': 1000
    },
    'required_fields': [
        'name',
        'brand',
        'price'
    ],
    'Amazon': {
        'search': {
            'query': 'https://www.amazon.com/s/?field-keywords={}',
            'first_item': '//*[@id="result_0"]/div/div[3]/div[1]/a/@href',
            'first_item_fallback': '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href'
        },
        'fields': {
            'name': '//*[@id="productTitle"]/text()',
            'brand': '//*[@id="brand"]/text()',
            'brand_fallback': '//*[@id="bylineInfo"]/text()',
            'brand_link': '//*[@id="brand"]/@href',
            'brand_link_fallback': '//*[@id="bylineInfo"]/@href',
            'price': '//*[@id="priceblock_ourprice"]/text()',
            'availability': '//*[@id="availability"]/span/text()',
            'merchant': '//*[@id="merchant-info"]/text()',
            'ships_from': '//*[@id="shipsFromSoldBy_feature_div"]/text()',
            'shipping_date': '//*[@id="fast-track-message"]/text()',
            'n_resellers': '//*[@id="olp_feature_div"]/div/span/a/text()',
            #
            # TODO: I need Mike to point to these on an image
            #
            # 'prime': '',
            # 'business': '',
            # 'date': '',
            # 'sku': '',
            # 'fba': '',
            # 'ssa': '',
        }
    }
}
