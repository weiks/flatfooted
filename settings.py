
#
# TODO: I'm assumsing:
#
# - `sku` == `product
# - `date`, `search`, and `site` are specified by us (not site dependent)
#
# TODO: We should standarize names to avoid spreading variables in data frames
#

SETTINGS = {
    'save_raw_html': False,
    'random_proxies': False,
    'random_user_agents': True,
    'results_file_type': 'json',
    'timezone': 'America/Mexico_City',
    'search_strings': {
        'file': 'inputs/search-strings-re-test.csv',
        'variable': 'String',
        'sample': 10
    },
    'required_fields': [
        'name',
        'price'
    ],
    'sites': {
        # 'Amazon': {
        #     'search': {
        #         'query': 'https://www.amazon.com/s/?field-keywords={}',
        #         'first_item': [
        #             '//*[@id="result_0"]/div/div[3]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div[2]/div/div[2]/div[2]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="productTitle"]//text()'
        #         ],
        #         'brand': [
        #             '//*[@id="brand"]//text()',
        #             '//*[@id="bylineInfo"]//text()'
        #         ],
        #         'brand_link': [
        #             '//*[@id="brand"]//@href',
        #             '//*[@id="bylineInfo"]//@href'
        #         ],
        #         'price': [
        #             '//*[@id="priceblock_ourprice"]//text()',   # Regular price
        #             '//*[@id="priceblock_saleprice"]//text()'   # Sale price
        #         ],
        #         'availability': [
        #             '//*[@id="availability"]//text()'
        #         ],
        #         'ships_from': [
        #             '//*[@id="shipsFromSoldBy_feature_div"]//text()'
        #         ],
        #         'fast_track': [
        #             '//*[@id="fast-track-message"]//text()'
        #         ],
        #         'n_resellers': [
        #             '//*[@id="olp_feature_div"]//text()'
        #         ]
        #     }
        # }
        # 'Staples': {
        #     # NOTE: TEST: NO: JavaScript
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
        #             '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #             '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #             '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #             '//*[@id="getPrice"]/div[1]/div[2]//text()',
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
        # 'GWW': {
        #     # NOTE: TEST: NO: JavaScript
        #     'search': {
        #         'query': 'https://www.grainger.com/search?searchQuery={}',
        #         'first_item': [
        #             # TODO: Do we need JavaScript? Must be clicked?
        #             # '//*[@id="list-view--js"]/li[1]'
        #             '//*[@id="body"]/div[3]/div/header/h2/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="productPage"]/div[2]/h1//text()'
        #         ],
        #         'price': [
        #             '//*[@id="addItemsToCartFromIdp"]/div/div[1]/div/div[1]/div/div/span[2]/span[2]//text()'
        #         ],
        #         'item_id': [
        #             '//*[@id="productPage"]/div[2]/ul/li[1]/span//text()'
        #         ],
        #         'mfr_id': [
        #             '//*[@id="productPage"]/div[2]/ul/li[3]/span//text()'
        #         ],
        #         'unspsc': [
        #             '//*[@id="unspsc"]/span//text()'
        #         ],
        #         'brand': [
        #             '//*[@id="productPage"]/div[2]/a//text()'
        #         ],
        #         # 'per': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'shipping': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'drop_ship': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'get_this_price': [
        #         #     # TODO: Identify on page
        #         # ]
        #     }
        # },
        # 'Zoro': {
        #     # NOTE: TESTED: NO: JavaScript
        #     'search': {
        #         'query': 'https://www.zoro.com/search?q={}',
        #         'first_item': [
        #             '//*[@id="grid"]/li[1]/div/ul/li[1]/h5/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="single-sku"]/div[4]/h1/span//text()'
        #         ],
        #         'price': [
        #             '//*[@id="availability"]/h3/span[2]//text()'
        #         ],
        #         'in_stock': [
        #             '//*[@id="avl-info-icon"]/span//text()'
        #         ],
        #         'zoro_id': [
        #             '//*[@id="brand-name"]/strong/span//text()'
        #         ],
        #         'mfr_id': [
        #             '//*[@id="brand-name"]/span[3]//text()'
        #         ],
        #         'shipping_time': [
        #             '//*[@id="ships-from-lead-time-G1787563"]//text()'
        #         ]
        #     }
        # },
        # 'cdw': {
        #     # NOTE: TESTED: YES
        #     'search': {
        #         'query': 'https://www.cdw.com/shop/search/result.aspx?b={}',
        #         'first_item': [
        #             '//*[@id="main"]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/h2/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="primaryProductName"]/span//text()'
        #         ],
        #         'price': [
        #             # NOTE: The use of the content attribute. Due to the way
        #             # the site is programmed, is we use `//text()` in this case
        #             # we will get double results (the ones for the "text", and
        #             # for the "content").
        #             '//*[@id="singleCurrentItemLabel"]/span[2]/@content'
        #         ],
        #         'mfg_part': [
        #             '//*[@id="primaryProductPartNumbers"]/span[1]/span//text()'
        #         ],
        #         'cdw_part': [
        #             '//*[@id="primaryProductPartNumbers"]/span[3]//text()'
        #         ],
        #         # 'product_link': [
        #         #     # TODO: Identify in page
        #         # ],
        #         # 'ship': [
        #         #     # TODO: Identify in page
        #         # ],
        #         # 'ship2': [
        #         #     # TODO: Identify in page
        #         # ]
        #     }
        # },
        # 'cnxn': {
        #     # NOTE: TESTED: YES
        #     # NOTE: Incorrect usage of HTTPS codes (404 (Not Found) and 302 (Moved))
        #     'search': {
        #         'query': 'https://www.connection.com/IPA/Shop/Product/Search?SearchType=1&term={}',
        #         'first_item': [
        #             '//*[@id="listView"]/div/table/tbody/tr[1]/td[2]/div[1]/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="mainLayoutContainer"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div/h1//text()'
        #         ],
        #         'price': [
        #             '//*[@id="productDetail"]/div/div[4]/div[3]/div[1]/div[2]/div/div/span/span//text()'
        #         ],
        #         # 'product_link': [
        #         #     # TODO: Identify on page
        #         # ]
        #         # 'brand': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'cnxn_no': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'mfg_no': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'ship': [
        #         #     # TODO: Identify on page
        #         # ]
        #     }
        # },
        # 'tecd': {
        #     # NOTE: TEST: NO: Needs sign-in
        #     'search': {
        #         'query': 'https://shop.techdata.com/searchall?kw={}',
        #         'first_item': [
        #             '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[1]/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #         ],
        #         'price': [
        #         ],
        #         # 'product-link': [
        #         # ],
        #         # 'product': [
        #         # ],
        #         # 'msrp': [
        #         # ],
        #         # 'mrf_no': [
        #         # ],
        #         # 'tecd_no': [
        #         # ],
        #         # 'status': [
        #         # ]
        #     }
        # },
        # 'nsit': {
        #     # NOTE: TEST: NO: Needs ZIP
        #     'search': {
        #         'query': 'https://www.insight.com/en_US/search.html?q={}',
        #         'first_item': [
        #             '//*[@id="js-search-product-items"]/div[1]/div/div[4]/div/h3/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="js-product-detail-target"]/h1/a/@href'
        #         ],
        #         'price': [
        #             # TODO: Has a "Estimate the total price of this item" step
        #             #       before actually showing price, and requires ZIP.
        #             ''
        #         ],
        #         # 'product-link': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'product': [
        #         #     # TODO: Identify on page
        #         # ],
        #         'mfr_no': [
        #             '//*[@id="js-product-detail-pricing-target"]/table/tbody/tr/td[2]//text()'
        #         ],
        #         'insight_no': [
        #             '//*[@id="js-product-detail-pricing-target"]/table/tbody/tr/td[1]//text()'
        #         ],
        #         'avail': [
        #             # TODO: Same string here? (1)
        #             '//*[@id="product-avalialability-by-warehouse"]/span//text()'
        #         ],
        #         'in_stock': [
        #             # TODO: Same string here? (1)
        #             '//*[@id="product-avalialability-by-warehouse"]/span//text()'
        #         ]
        #     }
        # },
        # 'fast': {
        #     # NOTE: TESTED: YES
        #     'search': {
        #         'query': 'https://www.fastenal.com/products?term={}',
        #         'first_item': [
        #             # TODO: There's a "first item" per category and then
        #             # there's a table. I'm using the table results. Is
        #             # this ok?
        #             '//*[@id="attribute-table"]/div/div[2]/div[1]/div[2]/div[2]/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]//text()'
        #         ],
        #         'price': [
        #             # TODO: There are various types of prices mixed
        #             # ("wholesale", "retail", "online", and maybe others)
        #             '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div//text()'
        #         ],
        #         'brand': [
        #             '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[4]/td[2]/div/a/span//text()',
        #             '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[2]/div/a/span//text()',
        #         ],
        #         'fast_part_no': [
        #             '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]/div//text()'
        #         ],
        #         'unspsc': [
        #             '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/a//text()'
        #         ]
        #     }
        # },
        # 'AZO': {
        #     # NOTE: TESTED: NO: Double-hop, and asks for ZIP
        #     'search': {
        #         'query': '',
        #         'first_item': [
        #             '//*[@id="idEngineOilPanGasket"]/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #         ],
        #         'price': [
        #         ]
        #     }
        # },
        # 'BUNZL': {
        #     # NOTE: TESTED: YES
        #     'search': {
        #         'query': 'https://www.bunzlpd.com/catalogsearch/result/?q={}',
        #         'first_item': [
        #             '//*[@id="content"]/div/div[3]/div[2]/div[3]/ul/li[1]/div/a[1]/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/h1//text()'
        #         ],
        #         'price': [
        #             # TODO: There are various prices for the different options.
        #             # I'm taking the first one, is this ok?
        #             '//*[@id="collateral-tabs"]/dd[1]/div/table/tbody/tr[1]/td[5]/span/span//text()'
        #         ],
        #         'item_no': [
        #             '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/p[1]//text()'
        #         ],
        #         # 'min_price': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'regular_price': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'shipping': [
        #         #     # TODO: Identify on page
        #         # ]
        #     }
        # },
        # 'pcmi': {
        #     # NOTE: TESTED: NO: Repeated with `nsit` site
        #     'search': {
        #         'query': 'https://www.insight.com/en_US/search.html?q={}',
        #         'first_item': [
        #             '//*[@id="js-search-product-items"]/div[1]/div/div[4]/div/h3/a/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #         ],
        #         'price': [
        #         ]
        #     }
        # },
        # 'MSM': {
        #     # NOTE: TESTED: NO: Double-hop
        #     'search': {
        #         'query': 'https://www.mscdirect.com/browse/tn/?searchterm={}',
        #         'first_item': [
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #         ],
        #         'price': [
        #         ],
        #         'brand': [
        #         ],
        #         'msc_part_no': [
        #         ],
        #         'upc_no': [
        #         ],
        #         'cat_1': [
        #         ],
        #         'cat_2': [
        #         ],
        #         'in_stock': [
        #         ],
        #         'mfr_no': [
        #         ]
        #     }
        # },
        # 'hdss': {
        #     # NOTE: TESTED: YES
        #     'search': {
        #         'query': 'https://hdsupplysolutions.com/shop/SearchDisplay?searchTerm={}',
        #         'first_item': [
        #             '//*[@id="ProdDescFormatLink_316110"]/@href'
        #         ]
        #     },
        #     'fields': {
        #         'name': [
        #             '//*[@id="product_detail_h1"]//text()'
        #         ],
        #         'price': [
        #             '//*[@id="product-detail-price-tier"]/ul/li/div/div[2]//text()'
        #         ],
        #         'unspsc': [
        #             '//*[@id="make"]/table/tbody/tr[1]/td[2]//text()'
        #         ],
        #         'brand': [
        #             '//*[@id="make"]/table/tbody/tr[2]/td[2]//text()'
        #         ],
        #         'part_no': [
        #             '//*[@id="make"]/table/tbody/tr[3]/td[2]//text()'
        #         ],
        #         'shipping_details': [
        #             # TODO: Various fields available, trying to get all of them
        #             '//*[@id="product-detail-shipping"]/ul//text()'
        #         ],
        #         # 'instock': [
        #         #     # TODO: Button for "check stock" but requires account
        #         # ],
        #         # 'price_tier': [
        #         #     # TODO: Identify on page
        #         # ],
        #         # 'priceq': [
        #         #     # TODO: Identify on page
        #         # ]
        #     }
        # },
        # 'esnd': {
        #     # NOTE: TESTED: YES
        #     # TODO: URLs being detected as duplicates, maybe it's the `#`
        #     'search': {
        #         'query': 'http://biggestbook.com/ui/catalog.html#/search?keyword={}',
        #         'first_item': [
        #             '//*[@id="bbMain"]/div/div/main/div/div/div/div[4]/div[3]/div[1]/bb-product/div/div/div[8]/div[2]/@href'
        #         ]
        #     },
        #     'fields': {
        #         # TODO: I don't have an specification for this site
        #         'name': [
        #             '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[2]/span//text()'
        #         ],
        #         'price': [
        #             '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[6]/div[1]/div[1]/div[2]//text()'
        #         ]
        #     }
        # }
    }
}
