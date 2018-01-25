
SETTINGS = {
    'save_raw_html': False,
    'random_proxies': False,
    'random_user_agents': True,
    'results_file_type': 'json',
    'timezone': 'America/Mexico_City',
    'search_strings': {
        'file': 'inputs/search-strings-full.csv',
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
        #             '//*[@id="result_0"]/div/div[4]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div[3]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div[2]/div/div[2]/div[2]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href',
        #             '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="noResultsTitle"]//text()',
        #                 '//*[@id="s-result-count"]//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="productTitle"]//text()'
        #             ],
        #             'brand': [
        #                 '//*[@id="brand"]//text()',
        #                 '//*[@id="bylineInfo"]//text()'
        #             ],
        #             'brand_link': [
        #                 '//*[@id="brand"]//@href',
        #                 '//*[@id="bylineInfo"]//@href'
        #             ],
        #             'price': [
        #                 '//*[@id="priceblock_ourprice"]//text()',
        #                 '//*[@id="priceblock_saleprice"]//text()'
        #             ],
        #             'availability': [
        #                 '//*[@id="availability"]//text()'
        #             ],
        #             'ships_from': [
        #                 '//*[@id="shipsFromSoldBy_feature_div"]//text()'
        #             ],
        #             'fast_track': [
        #                 '//*[@id="fast-track-message"]//text()'
        #             ],
        #             'n_resellers': [
        #                 '//*[@id="olp_feature_div"]//text()'
        #             ]
        #         }
        #     }
        # },
        # 'cdw': {
        #     'search': {
        #         'query': 'https://www.cdw.com/shop/search/result.aspx?b={}',
        #         'first_item': [
        #             '//*[@id="main"]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/h2/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="main"]/div/div/div[2]/div[2]/div[1]//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="primaryProductName"]/span//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="singleCurrentItemLabel"]/span[2]//text()'
        #             ],
        #             'mfg': [
        #                 '//*[@id="primaryProductPartNumbers"]/span[1]/span//text()'
        #             ],
        #             'cdw': [
        #                 '//*[@id="primaryProductPartNumbers"]/span[3]//text()'
        #             ],
        #             'availability': [
        #                 '//*[@id="primaryProductAvailability"]//text()'
        #             ]
        #         }
        #     }
        # },
        # 'fast': {
        #     'search': {
        #         'query': 'https://www.fastenal.com/products?term={}',
        #         'first_item': [
        #             '//*[@id="attribute-table"]/div/div[2]/div[1]/div[2]/div[2]/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="refine-by-attribute"]/span//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]//text()'
        #             ],
        #             'price': [
        #                 '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div//text()'
        #             ],
        #             #
        #             # NOTE: Since the table is dynamice (fields can change
        #             # order/location without that location being known aprior),
        #             # Mike opted for us to simply get the whole table instead
        #             # of trying to parse it. This may change once the results
        #             # are evaluated.
        #             #
        #             # 'brand': [
        #             #     '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[4]/td[2]/div/a/span//text()',
        #             #     '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[2]/div/a/span//text()',
        #             # ],
        #             # 'site_id': [
        #             #     '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]/div//text()'
        #             # ],
        #             # 'unspsc': [
        #             #     '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/a//text()'
        #             # ]
        #             'table': [
        #                 '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table//text()'
        #             ]
        #         }
        #     }
        # },
        # 'BUNZL': {
        #     'search': {
        #         'query': 'https://www.bunzlpd.com/catalogsearch/result/?q={}',
        #         'first_item': [
        #             '//*[@id="content"]/div/div[3]/div[2]/div[3]/ul/li[1]/div/a[1]/@href',
        #             '//*[@id="content"]/div/div[3]/div[2]/div[3]/ul/li[1]/div/a[1]/@href',
        #             '//*[@id="content"]/div/div[3]/div[2]/div[2]/ul/li[1]/div/a[1]/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="content"]/div/div[3]/p[1]//text()',
        #                 '//*[@id="content"]/div/div[3]/div[2]/div[1]/div[1]/div[1]//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/h1//text()',
        #             ],
        #             'price': [
        #                 '//*[@id="collateral-tabs"]/dd[1]/div/table/tbody/tr[1]/td[5]/span/span//text()'
        #             ],
        #             'min_price': [
        #                 '//*[@id="collateral-tabs"]/dd[1]/div/table/tbody/tr[1]/td[5]/ul/li/span//text()'
        #             ],
        #             'site_id': [
        #                 '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/p[1]//text()',
        #             ],
        #             'availability': [
        #                 '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/p[2]//text()'
        #             ]
        #         }
        #     }
        # },
        # 'pcmi': {
        #     'search': {
        #         'query': 'http://www.tigerdirect.com/applications/SearchTools/search.asp?keywords={}',
        #         'first_item': [
        #             '//*[@id="mainC"]/div/div[3]/div[2]/div[2]/div[2]/h3/a/@href',
        #             '//*[@id="mainC"]/div/div[3]/div/div[2]/div[2]/h3/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="mainC"]/div/div[3]/div/div[1]/div[2]/div[1]//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="ProductReview"]/div[2]/div[2]/div[1]/h1//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="ProductReview"]/div[2]/div[2]/dl/dd//text()'
        #             ],
        #             'site_id': [
        #                 '//*[@id="ProductReview"]/div[2]/div[2]/div[1]/span//text()'
        #             ],
        #             'availability': [
        #                 '//*[@id="ProductReview"]/div[2]/div[2]/div[2]/dl//text()'
        #             ]
        #         }
        #     }
        # },
        # 'Staples': {
        #     # NOTE: TEST: NO: JavaScript
        #     'search': {
        #         'query': 'https://www.staples.com/{0}/directory_{0}?',
        #         'first_item_css': [
        #             'div.product-info > a::attr(href)'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 ''
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="mainNgApp"]/div/div[2]/div/div[1]/h1//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #                 '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #                 '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
        #                 '//*[@id="getPrice"]/div[1]/div[2]//text()',
        #             ],
        #             'availability': [
        #                 '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div//text()',
        #             ],
        #             'ships_from': [
        #                 '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[4]/div[2]/div//text()'
        #             ],
        #             'model': [
        #                 '//*[@id="mainNgApp"]/div/div[2]/div/div[1]/div/ul/li[2]/span//text()'
        #             ]
        #         }
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
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="productPage"]/div[2]/h1//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="addItemsToCartFromIdp"]/div/div[1]/div/div[1]/div/div/span[2]/span[2]//text()'
        #             ],
        #             'item_id': [
        #                 '//*[@id="productPage"]/div[2]/ul/li[1]/span//text()'
        #             ],
        #             'mfr_id': [
        #                 '//*[@id="productPage"]/div[2]/ul/li[3]/span//text()'
        #             ],
        #             'unspsc': [
        #                 '//*[@id="unspsc"]/span//text()'
        #             ],
        #             'brand': [
        #                 '//*[@id="productPage"]/div[2]/a//text()'
        #             ],
        #             # 'per': [
        #             #     # TODO: Identify on page
        #             # ],
        #             # 'availability': [
        #             #     # TODO: Identify on page
        #             # ],
        #             # 'drop_ship': [
        #             #     # TODO: Identify on page
        #             # ],
        #             # 'get_this_price': [
        #             #     # TODO: Identify on page
        #             # ]
        #     }
        # },
        # 'Zoro': {
        #     # NOTE: TESTED: NO: JavaScript
        #     'search': {
        #         'query': 'https://www.zoro.com/search?q={}',
        #         'first_item': [
        #             '//*[@id="grid"]/li[1]/div/ul/li[1]/h5/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="single-sku"]/div[4]/h1/span//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="availability"]/h3/span[2]//text()'
        #             ],
        #             'availability': [
        #                 '//*[@id="avl-info-icon"]/span//text()'
        #             ],
        #             'site_id': [
        #                 '//*[@id="brand-name"]/strong/span//text()'
        #             ],
        #             'mfr_id': [
        #                 '//*[@id="brand-name"]/span[3]//text()'
        #             ],
        #             'shipping_time': [
        #                 '//*[@id="ships-from-lead-time-G1787563"]//text()'
        #             ]
        #         }
        #     }
        # },
        # 'cnxn': {
        #     # NOTE: TESTED: YES
        #     # NOTE: Incorrect usage of HTTPS codes (404 (Not Found) and 302 (Moved))
        #     'search': {
        #         'query': 'https://www.connection.com/IPA/Shop/Product/Search?SearchType=1&term={}',
        #         'first_item': [
        #             '//*[@id="listView"]/div/table/tbody/tr[1]/td[2]/div[1]/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="mainLayoutContainer"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div/h1//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="productDetail"]/div/div[4]/div[3]/div[1]/div[2]/div/div/span/span//text()'
        #             ],
        #             # 'brand': [
        #             #     # TODO: Identify on page
        #             # ],
        #             # 'cnxn': [
        #             #     # TODO: Identify on page
        #             # ],
        #             # 'mfg': [
        #             #     # TODO: Identify on page
        #             # ],
        #             # 'availability': [
        #             #     # TODO: Identify on page
        #             # ]
        #         }
        #     }
        # },
        # 'tecd': {
        #     # NOTE: TEST: NO: Needs sign-in
        #     'search': {
        #         'query': 'https://shop.techdata.com/searchall?kw={}',
        #         'first_item': [
        #             '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[1]/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #             ],
        #             'price': [
        #             ],
        #             # 'msrp': [
        #             # ],
        #             # 'mrf': [
        #             # ],
        #             # 'site_id': [
        #             # ],
        #             # 'status': [
        #             # ]
        #         }
        #     }
        # },
        # 'nsit': {
        #     # NOTE: TEST: NO: Needs ZIP
        #     'search': {
        #         'query': 'https://www.insight.com/en_US/search.html?q={}',
        #         'first_item': [
        #             '//*[@id="js-search-product-items"]/div[1]/div/div[4]/div/h3/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="js-product-detail-target"]/h1/a/@href'
        #             ],
        #             'price': [
        #                 # Has a "Estimate the total price of this item" step
        #                 # before actually showing price, and requires ZIP
        #                 '//*[@id="js-product-detail-pricing-target"]/div[3]/div[1]/div/div[1]/p[2]//text()'
        #             ],
        #             'site_id': [
        #                 '//*[@id="js-product-detail-pricing-target"]/table/tbody/tr/td[1]//text()'
        #             ],
        #             'mfr': [
        #                 '//*[@id="js-product-detail-pricing-target"]/table/tbody/tr/td[2]//text()'
        #             ],
        #             'availability': [
        #                 '//*[@id="product-avalialability-by-warehouse"]/span//text()'
        #             ]
        #         }
        #     }
        # },
        # 'AZO': {
        #     # NOTE: TESTED: NO: Double-hop, and asks for ZIP
        #     'search': {
        #         'query': '',
        #         'first_item': [
        #             '//*[@id="idEngineOilPanGasket"]/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #             ],
        #             'price': [
        #             ]
        #         }
        #     }
        # },
        # 'MSM': {
        #     # NOTE: TESTED: NO: Double-hop
        #     'search': {
        #         'query': 'https://www.mscdirect.com/browse/tn/?searchterm={}',
        #         'first_item': [
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #             ],
        #             'price': [
        #             ],
        #             'brand': [
        #             ],
        #             'msc': [
        #             ],
        #             'upc': [
        #             ],
        #             'cat_1': [
        #             ],
        #             'cat_2': [
        #             ],
        #             'availability': [
        #             ],
        #             'mfr': [
        #             ]
        #         }
        #     }
        # },
        # 'hdss': {
        #     # NOTE: TESTED: YES
        #     'search': {
        #         'query': 'https://hdsupplysolutions.com/shop/SearchDisplay?searchTerm={}',
        #         'first_item': [
        #             # '//*[@id="productsForm"]/div[1]/div/div[3]',
        #             '//*[@id="productsForm"]/div[1]/div/div[3]/div[1]/div[1]/h2/a/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="total_results"]//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="product_detail_h1"]//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="product-detail-price-tier"]/ul/li/div/div[2]//text()'
        #             ],
        #             'unspsc': [
        #                 '//*[@id="make"]/table/tbody/tr[1]/td[2]//text()'
        #             ],
        #             'brand': [
        #                 '//*[@id="make"]/table/tbody/tr[2]/td[2]//text()'
        #             ],
        #             'site_id': [
        #                 '//*[@id="make"]/table/tbody/tr[3]/td[2]//text()'
        #             ],
        #             'availability': [
        #                 '//*[@id="product-detail-shipping"]/ul//text()'
        #             ]
        #         }
        #     }
        # },
        # 'esnd': {
        #     # NOTE: TESTED: YES
        #     # TODO: URLs being detected as duplicates, maybe it's the `#`
        #     'search': {
        #         'query': 'http://biggestbook.com/ui/catalog.html#/search?keyword={}',
        #         'first_item': [
        #             '//*[@id="bbMain"]/div/div/main/div/div/div/div[4]/div[3]/div[1]/bb-product/div/div/div[8]/div[2]/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             # TODO: I don't have an specification for this site
        #             'name': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[2]/span//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[6]/div[1]/div[1]/div[2]//text()'
        #             ]
        #         }
        #     }
        # }
    }
}
