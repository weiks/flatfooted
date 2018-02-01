
SETTINGS = {
    'save_html': False,
    'random_proxies': False,
    'random_user_agents': True,
    'timezone': 'America/Mexico_City',
    'search_strings': {
        'file': 'inputs/search-strings-full.csv',
        # 'file': 'inputs/search-strings-re-test.csv',
        'variable': 'String',
        'sample': None
    },
    'required_fields': [
        'name',
        'price'
    ],
    'sites': {
        #
        # Standard
        #
        'AMZN': {
            'base_url': 'https://www.amazon.com',
            'search': {
                'query': 'https://www.amazon.com/s/?field-keywords={}',
                'first_item': [
                    '//*[@id="result_0"]/div/div[4]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div[3]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div[2]/div/div[2]/div[2]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href',
                    '//*[@id="result_0"]/div/div/div/div[2]/div[1]/div/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="s-result-count"]//text()'
                    ],
                    'results_description': [
                        '//*[@id="noResultsTitle"]//text()'
                    ]
                }
            },
            'item': {
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
                        '//*[@id="priceblock_ourprice"]//text()',
                        '//*[@id="priceblock_saleprice"]//text()'
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
        },
        'CDW': {
            'base_url': 'https://www.cdw.com',
            'search': {
                'query': 'https://www.cdw.com/search/?key={}',
                'first_item': [
                    '//*[@id="main"]/div/div/div[2]/div[4]/div[1]/div[3]/div[1]/h2/a/@href',
                    '//*[@id="main"]/div/div/div[2]/div[4]/div[1]/div[2]/div[1]/h2/a/@href',
                    '//*[@id="main"]/div/div/div[2]/div[5]/div[1]/div[2]/div[1]/h2/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="main"]/div/div/div[2]/div[2]/div[1]//text()'
                    ],
                    'results_description': [
                        '//*[@id="main"]/div/div/div[2]/div[3]/div[1]//text()',
                        '//*[@id="main"]/div/div/div/div[1]/span//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="primaryProductName"]/span//text()'
                    ],
                    'price': [
                        '//*[@id="singleCurrentItemLabel"]/span[2]//text()'
                    ],
                    'mfg': [
                        '//*[@id="primaryProductPartNumbers"]/span[1]/span//text()'
                    ],
                    'cdw': [
                        '//*[@id="primaryProductPartNumbers"]/span[3]//text()'
                    ],
                    'availability': [
                        '//*[@id="primaryProductAvailability"]//text()'
                    ]
                }
            }
        },
        'FAST': {
            'base_url': 'https://www.fastenal.com',
            'search': {
                'query': 'https://www.fastenal.com/products?term={}',
                'first_item': [
                    '//*[@id="attribute-table"]/div/div[2]/div[1]/div[2]/div[2]/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="refine-by-attribute"]/span//text()'
                    ],
                    'results_description': [
                        ''
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]//text()'
                    ],
                    'price': [
                        '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div//text()'
                    ],
                    'table': [
                        '/html/body/main/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/table//text()'
                    ]
                }
            }
        },
        'BUNZL': {
            'base_url': 'https://www.bunzlpd.com',
            'search': {
                'query': 'https://www.bunzlpd.com/catalogsearch/result/?q={}',
                'first_item': [
                    '//*[@id="content"]/div/div[3]/div[2]/div[3]/ul/li[1]/div/a[1]/@href',
                    '//*[@id="content"]/div/div[3]/div[2]/div[3]/ul/li[1]/div/a[1]/@href',
                    '//*[@id="content"]/div/div[3]/div[2]/div[2]/ul/li[1]/div/a[1]/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="content"]/div/div[3]/p[1]//text()',
                        '//*[@id="content"]/div/div[3]/div[2]/div[1]/div[1]/div[1]//text()'
                    ],
                    'results_description': [
                        ''
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/h1//text()',
                    ],
                    'price': [
                        '//*[@id="collateral-tabs"]/dd[1]/div/table/tbody/tr[1]/td[5]/span/span//text()'
                    ],
                    'min_price': [
                        '//*[@id="collateral-tabs"]/dd[1]/div/table/tbody/tr[1]/td[5]/ul/li/span//text()'
                    ],
                    'site_id': [
                        '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/p[1]//text()',
                    ],
                    'availability': [
                        '//*[@id="content"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/p[2]//text()'
                    ]
                }
            }
        },
        'PCMI': {
            'base_url': 'http://www.tigerdirect.com',
            'search': {
                'query': 'http://www.tigerdirect.com/applications/SearchTools/search.asp?keywords={}',
                'first_item': [
                    '//*[@id="mainC"]/div/div[3]/div[2]/div[2]/div[2]/h3/a/@href',
                    '//*[@id="mainC"]/div/div[3]/div/div[2]/div[2]/h3/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="mainC"]/div/div[3]/div/div[1]/div[2]/div[1]//text()'
                    ],
                    'results_description': [
                        '//*[@id="mainC"]/div/div[3]/h1//text()',
                        '//*[@id="mainC"]/table/tbody/tr[1]/td[3]//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="ProductReview"]/div[2]/div[2]/div[1]/h1//text()'
                    ],
                    'price': [
                        '//*[@id="ProductReview"]/div[2]/div[2]/dl/dd//text()'
                    ],
                    'site_id': [
                        '//*[@id="ProductReview"]/div[2]/div[2]/div[1]/span//text()'
                    ],
                    'availability': [
                        '//*[@id="ProductReview"]/div[2]/div[2]/div[2]/dl//text()'
                    ]
                }
            }
        },
        'HDSS': {
            'base_url': 'https://hdsupplysolutions.com',
            'search': {
                'query': 'https://hdsupplysolutions.com/shop/SearchDisplay?searchTerm={}',
                'first_item': [
                    '//*[@id="productsForm"]/div[1]/div/div[3]/div[1]/div[1]/h2/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="total_results"]//text()'
                    ],
                    'results_description_css': [
                        'div.results_description::text'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="product_detail_h1"]//text()'
                    ],
                    'price': [
                        '//*[@id="product-detail-price-tier"]/ul/li/div/div[2]//text()'
                    ],
                    'unspsc': [
                        '//*[@id="make"]/table/tbody/tr[1]/td[2]//text()'
                    ],
                    'brand': [
                        '//*[@id="make"]/table/tbody/tr[2]/td[2]//text()'
                    ],
                    'site_id': [
                        '//*[@id="make"]/table/tbody/tr[3]/td[2]//text()'
                    ],
                    'availability': [
                        '//*[@id="product-detail-shipping"]/ul//text()'
                    ]
                }
            }
        },
        'CNXN': {
            'base_url': 'https://www.connection.com',
            'search': {
                'query': 'https://www.connection.com/IPA/Shop/Product/Search?SearchType=1&term={}',
                'first_item': [
                    '//*[@id="listView"]/div/table/tbody/tr[1]/td[2]/div[1]/a/@href'
                ],
                'auto_redirected_css': [
                    '#productDetail::text'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="searchResultContainer"]/div[1]/div[1]/span//text()'
                    ],
                    'results_description': [
                        '//*[@id="search-content"]/div/div[2]/p/strong//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="mainLayoutContainer"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div/h1//text()'
                    ],
                    'price': [
                        '//*[@id="productDetail"]/div/div[4]/div[3]/div[1]/div[2]/div/div/span/span//text()'
                    ],
                    'brand': [
                        '//*[@id="productNameLink"]/a//text()'
                    ],
                    'site_id': [
                        '//*[@id="productSku"]//text()'
                    ],
                    'mfr': [
                        '//*[@id="productManufacturerPartNumber"]//text()'
                    ],
                    'shipping': [
                        '//*[@id="productEstimatedShipping"]//text()'
                    ],
                    'availability': [
                        '//*[@id="productAvailability"]//text()'
                    ]
                }
            }
        },
        #
        # JavaScript
        #
        'ZORO': {
            'javascript': True,
            'base_url': 'https://www.zoro.com',
            'search': {
                'query': 'https://www.zoro.com/search?q={}',
                'first_item': [
                    '//*[@id="grid"]/li[1]/div/ul/li[1]/h5/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="part_content"]/div[3]/div[3]/div[1]/div[1]//text()',
                        '//*[@id="part_content"]/div[3]/div[3]/div[2]/div[1]/div//text()',
                        '//*[@id="part_content"]/div[3]/div[3]/div[1]/div[2]/div//text()',
                        '//*[@id="part_content"]/div[3]/div[3]/div[2]/div[2]/div//text()'
                    ],
                    'results_description': [
                        '//*[@id="part_content"]/div[3]/div[3]/div[2]/div[1]//text()',
                        '//*[@id="part_content"]/div[1]/div[2]//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="single-sku"]/div[4]/h1/span//text()'
                    ],
                    'price': [
                        '//*[@id="availability"]/h3//text()'
                    ],
                    'availability': [
                        '//*[@id="availability"]/div[1]//text()'
                    ],
                    'shipping': [
                        '//*[@id="availability"]/div[2]//text()'
                    ],
                    'site_id': [
                        '//*[@id="brand-name"]/strong/span//text()'
                    ],
                    'mfr': [
                        '//*[@id="brand-name"]/span[3]//text()'
                    ]
                }
            }
        },
        'GWW': {
            'base_url': 'https://www.grainger.com',
            'search': {
                'query': 'https://www.grainger.com/search?searchQuery={}',
                'first_item': [
                    '//*[@id="body"]/div[3]/div/header/h2/a/@href'
                ],
                'auto_redirected_css': [
                    '#productPage > div.head-container.clearfix > h1::text'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="header-breadcrumb-container"]/div[3]//text()'
                    ],
                    'results_description': [
                        '//*[@id="main-content"]/div[1]/h1//text()',
                        '//*[@id="messaging-container"]//text()',
                        '//*[@id="header-breadcrumb-container"]/h1/span//text()',
                        '//*[@id="pageHeader"]//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="productPage"]/div[2]/h1//text()'
                    ],
                    'price': [
                        '//*[@id="addItemsToCartFromIdp"]/div/div[1]/div/div[1]/div/div/span[2]/span[2]//text()'
                    ],
                    'site_id': [
                        '//*[@id="productPage"]/div[2]/ul/li[1]/span//text()'
                    ],
                    'mfr': [
                        '//*[@id="productPage"]/div[2]/ul/li[3]/span//text()'
                    ],
                    'unspsc': [
                        '//*[@id="unspsc"]/span//text()'
                    ],
                    'brand': [
                        '//*[@id="productPage"]/div[2]/a//text()'
                    ]
                }
            }
        },
        'NSIT': {
            'javascript': True,
            'base_url': 'https://www.insight.com',
            'search': {
                'query': 'https://www.insight.com/en_US/search.html?q={}',
                'first_item': [
                    '//*[@id="js-search-product-items"]/div[1]/div/div[4]/div/h3/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="buy-counter"]/span//text()'
                    ],
                    'results_description': [
                        '//*[@id="js-search-product-items"]/div/div/h4//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="js-product-detail-target"]/h1//text()'
                    ],
                    'price': [
                        '//*[@id="js-product-detail-pricing-target"]/div[3]/div[1]/div/div[1]/p[2]//text()'
                    ],
                    'site_id': [
                        '//*[@id="js-product-detail-pricing-target"]/table/tbody/tr/td[1]//text()'
                    ],
                    'mfr': [
                        '//*[@id="js-product-detail-pricing-target"]/table/tbody/tr/td[2]//text()'
                    ],
                    'availability': [
                        '//*[@id="product-avalialability-by-warehouse"]/span//text()'
                    ]
                }
            }
        },
        'STAPLES': {
            'javascript': True,
            'base_url': 'https://www.staples.com',
            'search': {
                'query': 'https://www.staples.com/{0}/directory_{0}?',
                'first_item_css': [
                    'div.product-info > a::attr(href)'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="rightRailApp"]/div[1]/div/div[1]//text()'
                    ],
                    'results_description': [
                        '/html/body/div[3]/h1//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="mainNgApp"]/div/div[2]/div/div[1]/h1//text()'
                    ],
                    'price': [
                        '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
                        '//*[@id="getPrice"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
                        '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span//text()',
                        '//*[@id="getPrice"]/div[1]/div[2]//text()',
                    ],
                    'availability': [
                        '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div//text()',
                    ],
                    'ships_from': [
                        '//*[@id="getPrice"]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[4]/div[2]/div//text()'
                    ],
                    'model': [
                        '//*[@id="mainNgApp"]/div/div[2]/div/div[1]/div/ul/li[2]/span//text()'
                    ]
                }
            }
        },
        # 'ESND': {
        #     'javascript': True,
        #     'base_url': 'http://biggestbook.com',
        #     'search': {
        #         'query': 'http://biggestbook.com/ui/catalog.html#/search?keyword={}',
        #         'first_item': [
        #             '//*[@id="bbMain"]/div/div/main/div/div/div/div[4]/div[3]/div[1]/bb-product/div/div/div[8]/div[2]/@href',
        #             '//*[@id="bbMain"]/div/div/main/div/div/div/div[4]/div[2]/div[1]/bb-product/div/div/div[8]/div[2]/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div[4]/bb-views[1]/div/div/div/span[1]/bb-count//text()',
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div[1]/span//text()'
        #             ],
        #             'results_description': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div[1]/span//text()'
        #             ]
        #         }
        #     },
        #     'item': {
        #         'fields': {
        #             'name': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[2]/span//text()'
        #             ],
        #             'price': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[6]/div[1]/div[1]/div[2]//text()'
        #             ],
        #             'site_id': [
        #                 '//*[@id="bbMain"]/div/div/main/div/div/div/div/div[1]/bb-product/div/div/div[8]/div[3]/span//text()'
        #             ]
        #         }
        #     }
        # },
        #
        # Search Page
        #
        'TECD': {
            'base_url': 'https://techdata.com',
            'search': {
                'query': 'https://shop.techdata.com/searchall?kw={}',
                'fields': {
                    'number_of_results': [
                        '//*[@id="productSearchPageContainer"]/div[1]/div[2]/span[1]//text()'
                    ],
                    'results_description': [
                        '//*[@id="productSearchPageContainer"]/div[3]//text()',
                        '//*[@id="productSearchResults"]/div/h1//text()'
                    ],
                    'name': [
                        '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[1]//text()'
                    ],
                    'price': [
                        '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[2]/div/div[1]/div//text()'
                    ],
                    'site_id': [
                        '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[1]/span//text()'
                    ],
                    'mfr': [
                        '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/span//text()'
                    ],
                    'upc_ean': [
                        '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[3]/span/span//text()'
                    ],
                    'status': [
                        '//*[@id="productSearchResults"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div//text()'
                    ]
                }
            }
        },
        #
        # Double-hops
        #
        'MSM': {
            'base_url': 'https://www.mscdirect.com',
            'search': {
                'query': 'https://www.mscdirect.com/browse/tn/?searchterm={}',
                'auto_redirected_css': [
                    '#listPriceDiv::text'
                ],
                'double_hop': [
                    '//*[@id="v4-browse-items-grid-1"]/div/div[1]/a/@href'
                ],
                'first_item': [
                    '//*[@id="v4-tn-items-box"]/div[1]/div/div[2]/h4/a/@href'
                ],
                'fields': {
                    'number_of_results': [
                        '//*[@id="popluateAjaxResponse"]/h2[2]/div//text()',
                        '//*[@id="popluateAjaxResponse"]/h2/div//text()'
                    ],
                    'results_description': [
                        '//*[@id="popluateAjaxResponse"]/h2[1]//text()',
                        '//*[@id="v4-browse-content"]/div/div[1]/div/h3//text()',
                        '//*[@id="v4-browse-content"]/div[1]/h2//text()',
                        '//*[@id="popluateAjaxResponse"]/p//text()'
                    ]
                }
            },
            'item': {
                'fields': {
                    'name': [
                        '//*[@id="pdp-prod-title"]/h1//text()'
                    ],
                    'price': [
                        '//*[@id="listPriceDiv"]//text()'
                    ],
                    'brand': [
                        '//*[@id="pdp-spec-details"]/div[3]/div[2]//text()'
                    ],
                    'msc': [
                        '//*[@id="pdp-spec-details"]/div[4]/div[2]//text()'
                    ],
                    'mfr': [
                        '//*[@id="title_mfrPartNum"]//text()'
                    ],
                    'availability': [
                        '//*[@id="pdp-addtocart-notes-container"]/div[3]/p/strong//text()'
                    ]
                }
            }
        },
        # 'AZO': {
        #     'base_url': 'https://',
        #     'search': {
        #         'query': '',
        #         'first_item': [
        #             '//*[@id="idEngineOilPanGasket"]/@href'
        #         ],
        #         'fields': {
        #             'number_of_results': [
        #                 ''
        #             ],
        #             'results_description': [
        #                 ''
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
        # }
    }
}
