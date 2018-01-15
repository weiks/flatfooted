
SETTINGS = {
    'results_file_type': 'csv',
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
    'sites': {
        'Amazon': {
            'search': {
                'query': 'https://www.amazon.com/s/?field-keywords={}',
                'first_item': [
                    '//*[@id="result_0"]/div/div[3]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href'
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
                    '//*[@id="priceblock_ourprice"]//text()'
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
                ],
                #
                # CSS selectors (provided by Mike)
                #
                'results_css': [
                    'h2.a-size-base::text'
                ],
                'first_item_css': [
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal::text'
                ],
                'Prime_css': [
                    'li#result_0.s-result-item div.a-column > div.a-row.a-spacing-none::text'
                ],
                'shipping_css': [
                    'div.centerColAlign div.a-section.a-spacing-mini::text'
                ],
                'name_css': [
                    'h1.a-size-large span.a-size-large::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > h1.a-size-large span.a-size-large::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal h1.a-size-large span.a-size-large::text'
                ],
                'brand_css': [
                    'div.centerColAlign div.a-section a.a-link-normal::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > div.centerColAlign div.a-section a.a-link-normal::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal div.centerColAlign div.a-section a.a-link-normal::text'
                ],
                'price_css': [
                    'li#result_0.s-result-item span.sx-price::text'
                ],
                'ships_from_css': [
                    'div.centerColAlign div.a-section.a-spacing-mini::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > div.centerColAlign div.a-section.a-spacing-mini::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal div.centerColAlign div.a-section.a-spacing-mini::text'
                ],
                'shipping_date_css': [
                    'div.centerColAlign div.a-section div.a-section div.a-section::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > div.centerColAlign div.a-section div.a-section div.a-section::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal div.centerColAlign div.a-section div.a-section div.a-section::text'
                ],
                'business_css': [
                    'td.a-color-secondary::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > td.a-color-secondary::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal td.a-color-secondary::text'
                ],
                'site_css': [
                    'td:nth-of-type(1)::text',
                    'table td:nth-of-type(1)::text',
                    'table > td:nth-of-type(1)::text'
                ],
                'date_css': [
                    'td:nth-of-type(2)::text',
                    'table > td:nth-of-type(2)::text',
                    'table td:nth-of-type(2)::text'
                ],
                'sku_css': [
                    'a::text',
                    'table > a::text',
                    'table a::text'
                ],
                'FBA_css': [
                    'div.centerColAlign div.a-section.a-spacing-mini::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > div.centerColAlign div.a-section.a-spacing-mini::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal div.centerColAlign div.a-section.a-spacing-mini::text'
                ],
                'SSA_css': [
                    'div.centerColAlign div.a-section.a-spacing-mini::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal > div.centerColAlign div.a-section.a-spacing-mini::text',
                    'li#result_0.s-result-item div.a-row.a-spacing-small a.a-link-normal div.centerColAlign div.a-section.a-spacing-mini::text'
                ]
            }
        }
    }
}
