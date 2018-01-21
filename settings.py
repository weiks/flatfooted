
SETTINGS = {
    'save_raw_html': True,
    'random_proxies': False,
    'random_user_agents': True,
    'results_file_type': 'json',
    'timezone': 'America/Mexico_City',
    'search_strings': {
        'file': 'inputs/search-strings-re-test.csv',
        'variable': 'String',
        'sample': None
    },
    'required_fields': [
        'name',
        'price'
    ],
    'sites': {
        'Amazon': {
            'search': {
                'query': 'https://www.amazon.com/s/?field-keywords={}',
                'first_item': [
                    '//*[@id="result_0"]/div/div[3]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div[2]/div/div[2]/div[2]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div/a/@href'
                ]
            },
            'fields': {
                'name': [
                    '//*[@id="productTitle"]//text()'
                ],
                'brand': [
                    '//*[@id="brand"]//text()',
                    '//*[@id="bylineInfo"]//text()'
                ],
                'brand_link': [
                    '//*[@id="brand"]//@href',
                    '//*[@id="bylineInfo"]//@href'
                ],
                'price': [
                    '//*[@id="priceblock_ourprice"]//text()',   # Regular price
                    '//*[@id="priceblock_saleprice"]//text()'   # Sale price
                ],
                'availability': [
                    '//*[@id="availability"]//text()'
                ],
                'ships_from': [
                    '//*[@id="shipsFromSoldBy_feature_div"]//text()'
                ],
                'fast_track': [
                    '//*[@id="fast-track-message"]//text()'
                ],
                'n_resellers': [
                    '//*[@id="olp_feature_div"]//text()'
                ]
            }
        }
        # 'Staples': {
        #     'search': {
        #         'query': 'https://www.staples.com/{0}/directory_{0}?',
        #         'first_item_css': [
        #             'div.product-info > a::attr(href)'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="mainNgApp"]/div/div[2]/div/div[1]/h1//text()'
        #         ],
        #         'price': [
        #             # '//*[@id="getPrice"]/div[1]/div[2]//text()',
        #             '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #             '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #             '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()'
        #         ],
        #         'availability': [
        #             '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div//text()',
        #         ],
        #         'ships_from': [
        #             '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[4]/div[2]/div//text()'
        #         ],
        #         'model': [
        #             '//*[@id="mainNgApp"]/div/div[2]/div/div[1]/div/ul/li[2]/span//text()'
        #         ]
        #     }
        # }
    }
}
