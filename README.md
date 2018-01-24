
# Product Scraper

- Omar Trejo
- January, 2018

## Setup and Execute in Ubuntu 16 Environment

To execute the scraper in Ubuntu 16, you need to setup the development
environment by installing relevant Ubuntu 16 packages, as well as relevant
Python 3 packages. To do so, you may simply execute:

```
$ bash setup-environment.sh
```

### Settings

The `/settings.py` file (not to be confused with `utilities/settings.py`),
contains the settings that will be used for the scraping process. Currently, the
parameters that may be modified are:

- `random_proxies` (`True`/`False`): use a random proxy for each request.
- `random_user_agents` (`True`/`False`): use a random User Agent for each
  request.
  - In the case of Amazon, if no User Agent is used, the request is rejected.
- `results_file_type` (string: `csv`/`json`): file type that will be used to
  save results.
  - Given the current mechanism with all results (non-errors and errors) going
    into the same file, we need to use `json` and post-process to get `csv`
    files.
- `timezone` (valid timezone string): not used for now, but when scraping
  automatically, it will be used to select dates/times for scraping.
- `search_strings` (dictionary):
  - `file` (string): location of file that contains initial search strings.
  - `variable` (string): name of variable in the CSV that contains the strings
    used for searching.
  - `sample` (`None` or integer): If `None`, all the observations in the file
    will be used. If it's an integer, a random sample of size `sample` will be
    used.
- `required_fields` (list of strings): fields required for each sites.
- `sites` (dictionary): specification for the data to be scraped from each site.

### Execute

Once the `settings.py` have been adjusted, simply execute:

```
$ python3 main.py
```

The results will be in the `outputs/` directory.

## Tasks

### Phase 1

- [x] Join site and spreadsheet search strings
- [x] Test CSS selectors from `amzn` file
- [x] Removed 1,240 duplicates between site and spreaddsheet data
- [x] General search capability search-to-new-results-page
- [x] Test general search capability for Amazon
- [x] Use first-result mechanim to retrieve relevant item
- [ ] Environment installlation scripts for Ubuntu 16
  - Must be tested at least once by Mike

### Phase 2

- [x] Fix Twisted Reactor bug when scraping multiple sites
- [x] Test with two sites at the same time (use Staples)
- [x] Initial throttling mechanism
- [x] Initial randomized proxy mechanism
- [x] Initial randomize user-agent mechanism
- [x] Resarch best way to save results into database
  - Best done with `Item Pipelines`
- [x] Handle 429 (and possibly) other response codes
- [x] Include `search_string` to correlate results
- [x] Save information for unhandled requests
- [x] Update documentation
- [x] Remove non-ASCII characters that affect data post-processing
- [x] Retrieve fresh proxy list from API
  - Postponed due to requirement of only 5,000 / items / site / day
    - Currently testing if throttling is enough for this
    - If throttling is not enough, we can look again into proxies
  - Was actually implemented because the Staples site eturned HTTP status codes
    that indicated that, even though we're connecting only once every 2 or 3
    seconds, they detected it was the same IP and blocked us.
  - Note to implement this another scraper was created to retrieve live proxy
    data from ProxyDB. It was necessary because we need the "latest" proxies
    known to be within the US and which allow for HTTPS due to the
    automatic-redirection towards HTTPS (making HTTP proxies useless) mechanism
    implemented in Amazon and Staples.
    - This new scraper was implemente differently, it uses Selenium beacuse we
      need to execute JavaScript code which is used to obfuscate the proxy IPs
      and ports (to avoid people doing what we did, but that didn't stop us ;).
    - To be able to do this, we need to install Chromium and use the
      `chromedriver` included in the `utilities/` directory.

### Phase 3

- [x] Integrate "sale price" into "price" field
- [x] Separate field for "Currently unavailable"
- [x] Save raw HTML to re-scrape it if necessary without re-crawling
  - For example, an item which was search for on Amazon at a certain date, and
    with `search_string == RKLCDBKT`, is saved as:
    `outputs/html/Amazon_2018-01-21-02-32_RKLCDBKT.html`
  - If no HTML was saved for a response, it was because of a failure and we
    should further look into it.
- [x] Look for errors in the request-response cycle
  - When comparing number of lines in input file vs number of products in
    outputs file, we find that 3 out of 322 missing searches for Amazon.
  - The prolem was that the `Peachtree null` was repeated 3 times (4 in total)
    as a `search_string`, so these were the three extra observations that my
    code ignores because it treats them as duplicates of previous requests. This
    is to avoid unnecessary multiple requests, and that's the reason for the
    difference, not that we did not execute them or that they got an error I was
    not catching.
    - NOTE: If you look into full observations, they were actually different
      because the `SKU` variables was different for them, but the `String`
      variable (which is what I'm using to search sites) was the same. If we
      want to actually make them different, the `SKU` information should go
      inside the `String` information also.
- [x] Re-test 7 failed search cases with 2 new XPATHs for Amazon
  - Turns out that the correct number of searches that failed (meaning that they
    do return results, but the scraper did not detect them and marked them as
    not returning any results), was 12. These search terms are saved in the
    `inputs/search-strings-re-tests.csv` file.
  - New XPATHs have been integrated, and I've re-ordered them to make sure we go
    from specific to general, and thus are able to get "special" cases before
    they are "obscured" using a more "general" XPATH.
  - The last results show that we are now able to get all results correctly, as
    well as the information for the corresponding products.

### Phase 4

- [x] Insert metadata (`site_name` and `timestamp`) into results

- TODO: We should standarize all variable names (avoids variables unnecessarily
  spreading when loading data frames in R due to variable name uniqueness).
- TODO: Update site names to the ones Mike wants as values in data frame

From 15 sites:

- 14 were unique
- 2 require JavaScript
- 3 require input/data
- 2 require double-hops
- 7 were actually tested
- 3 worked fine so far

#### Group 1

- [ ] `GWW`   https://www.grainger.com/search?searchQuery=pen
  - Tested: No: Requires JavaScript
- [ ] `Zoro`  https://www.zoro.com/search?q=pen
  - Tested: No: Requires JavaScript

#### Group 2

- [x] `cdw`   https://www.cdw.com/shop/search/result.aspx?b=pen
  - Tested: Yes
  - Need to identify `product_link`, `ship`, and `ship2` on page
  - Explain reason why "CDW Part" is included in text but "Mfg. Part" is not
- [ ] `cnxn`  https://www.connection.com/IPA/Shop/Product/Search?term=pen
  - Tested: Yes
  - I'm getting a lot of 404 (Not Found) and 302 (Moved)
    - It seems that when an product is not found, they return a 404 instead of
      simply returning a 200. They are using HTML status code incorrectly. It
      doesn't affect functionality, but leaves 404's in the spreadsheet instead
      of leaving a 200 with a "research without results" indicator. Should we
      fix this?
    - When a result is actually returned (maybe when it's the only one), we're
      automatically redirected to the product page (with a 302), and that is
      messing up the mechanism. Need to look into this further. This definitely
      needs to be fixed.
  - Need to identify `product_link`, `brand`, `cnxn_no`, `mfg_no`, and `ship` on
    page
- [ ] `tecd`  https://shop.techdata.com/searchall?kw=pen
  - Tested: No: Needs sign-in
- [ ] `nsit`  https://www.insight.com/en_US/search.html?q=pen
  - Tested: No: Needs ZIP

#### Group 3

- [x] `fast`  https://www.fastenal.com/products?term=pen
  - Tested: Yes
  - There's a "first item" per category and then there's a table. I'm
    using the table results. Is this ok?
  - There are various types of prices mixed ("wholesale", "online", "unit", and
    maybe others). I'm trying to get all of them.
  - Some URLs returned by the site are using the `;` character in the URL
    and that's causing some fields to move in the spreadsheet.
  - There are no identifiers in the first/main table, so the fields can move
    around without ourselves knowing apriori where they will be. We need some
    kind of dynamic parsing for this (check each field until we find the word
    "Manufacturer" in one of the cells, and use the appropriate value)
- [ ] `AZO`   https://www.autozone.com/searchresult?searchText=pen
  - Tested: No: Double-hop and asks for ZIP

#### Group 4

- [x] `BUNZL` https://www.bunzlpd.com/catalogsearch/result/?q=pen
  - Tested: Yes
  - Need to identify `min_price`, `regular_price`, and `shipping` on page
- [ ] `pcmi`  https://www.insight.com/en_US/search.html?q=pen
  - Tested: No: Repeated URL with `nsit` site
- [ ] `MSM`   https://www.mscdirect.com/browse/tn/?searchterm=pen
  - Tested: No: Double-hop
- [ ] `hdss`  https://hdsupplysolutions.com/shop/SearchDisplay?searchTerm=pen
  - Tested: Yes
  - Not getting search results with the inputs we're using. Not sure if this is
    a problem with my code or if it's something else. Need to look into this
    futher.
  - Need to identify `price_tier` and `priceq` on page
  - `instock` button requires site account for checking
  - `shipping_details` has various fields, trying to get all of them
- [ ] `esnd`  http://biggestbook.com/ui/catalog.html#/search?keyword=pen
  - Tested: Yes
  - This is giving me problems (duplicated URLs), I need to look into this
    further, but I think it could be the reserved symbol `#`.
  - Need fields specification for this sitea

## Item analysis for Amazon

In the latest results we got from Amazon, there were 27 (out of , %) that did
not include price either in the "regular price" or the "reseller price". Those
URLs are listed below.

The reasons are for not getting results are:

| Number of cases | Reason                         | Can be fixed | Fix                                                                                             | Should fix | Note                              |
|-----------------|--------------------------------|--------------|-------------------------------------------------------------------------------------------------|------------|-----------------------------------|
|              10 | "Currently unavailable"        | No           |                                                                                                 |            |                                   |
|               8 | It's a book                    | Yes          | Extra XPATHs (Hardcover, Paperback, Kindle, Audiobook, MP3 CD, Mass Market Paperback, Audio CD) | ?          | Not all books have all categories |
|               2 | "Available from these sellers" | Sometimes    | Extra hop                                                                                       | ?          |                                   |
|               2 | "Sale price"                   | Yes          | Extra XPATH                                                                                     | ?          | Should we mix with "price"?       |
|               1 | "Temporarily out of stock"     | Yes          | Extra XPATH                                                                                     | ?          |                                   |
|               1 | It's a movie (type 1)          | Yes          | Extra XPATHs (Amazon Video, Blu-ray, DVD)                                                       | ?          |                                   |
|               1 | It's a movie (type 2)          | Yes          | Extra XPATH                                                                                     | ?          |                                   |
|               1 | It's a music CD                | Yes          | Extra XPATH                                                                                     | ?          |                                   |
|               1 | Standard product page          | Yes          | Extra XPATH                                                                                     | ?          | Should've been scraped            |

### "Currently unavailable"

1. https://www.amazon.com/Perforated-Sheet-Gauge-1200-Thick/dp/B001DE28AW/ref=sr_1_fkmr0_1/147-4712168-7006519?ie=UTF8&qid=1516474318&sr=8-1-fkmr0&keywords=0.04%22+x+0.1200%22+x+1+1%2F2%22+Carbide+30+Helix+4+Flute+Bright+Finish+Single+End+Square+Center+Cut+End+Mill
2. https://www.amazon.com/Circus-champions-Cheryl-Carol-Null/dp/B007FTDSJY/ref=sr_1_1/145-1648604-2739851?ie=UTF8&qid=1516474812&sr=8-1&keywords=Champion+null
3. https://www.amazon.com/Audiocodes-M1K-Msbg-ESBC-Remt-Impl-Lead-Schedule-M1K-MSBG-ESBC-REMT-I/dp/B00QQTGV6Q/ref=sr_1_fkmr0_1/133-9576551-1568128?ie=UTF8&qid=1516474517&sr=8-1-fkmr0&keywords=AUDIOCODES+MSWSBC%2FL+REMT+IMPL
4. https://www.amazon.com/Microsoft-MapPoint-2002-OLD-VERSION/dp/B00005B6U4/ref=sr_1_fkmr0_1/143-1324540-8363015?ie=UTF8&qid=1516475236&sr=8-1-fkmr0&keywords=Microsoft+WA5+00249
5. https://www.amazon.com/Hamilton-Forgemaster-Casters-Dia-X2-5-Precision/dp/B00JR1IDPM/ref=sr_1_1/145-8726779-6863320?ie=UTF8&qid=1516475343&sr=8-1&keywords=Precision+Tapered+Roller+Metal+Wheelhttps://www.amazon.com/Hamilton-Forgemaster-Casters-Dia-X2-5-Precision/dp/B00JR1IDPM/ref=sr_1_1/145-8726779-6863320?ie=UTF8&qid=1516475343&sr=8-1&keywords=Precision+Tapered+Roller+Metal+Wheel
6. https://www.amazon.com/Square-9007C66B1S22-NSFPGENUINE-9007-C66B1S/dp/B011OXVASW/ref=sr_1_1/139-4574136-1437254?ie=UTF8&qid=1516475487&sr=8-1&keywords=SQUARE+D+9007C66B1S22
7. https://www.amazon.com/Shepherd-Looks-Psalm-23/dp/0310274419/ref=sr_1_fkmr0_1/143-9175864-9580824?ie=UTF8&qid=1516475521&sr=8-1-fkmr0&keywords=Shepherd+3254MW
8. https://www.amazon.com/SUMCNMA431AC420K-Sumitomo-Carbide-Negative-Turning/dp/B071Y46W1C/ref=sr_1_fkmr0_1/130-1000088-6878668?ie=UTF8&qid=1516475581&sr=8-1-fkmr0&keywords=Sumitomo+191R292VNMG332ENZ+AC420K
9. https://www.amazon.com/Telemecanique-OsiSense-Standard-Slow-Break-Spring-Return/dp/B013WBU6HU/ref=sr_1_fkmr0_1/147-7425999-8531338?ie=UTF8&qid=1516475604&sr=8-1-fkmr0&keywords=Telemecanique+Sensors+XCMD2525L1
10. https://www.amazon.com/Pipe-Dipped-Galvanized-U-Bolt-pieces/dp/B076FBNRX9/ref=sr_1_1/146-3747027-7114248?ie=UTF8&qid=1516475633&sr=8-1&keywords=U17244.025.0037

### It's a book

1. https://www.amazon.com/Adobe-Photoshop-Elements-Classroom-Book/dp/0133987078/ref=sr_1_fkmr0_1/147-4532136-9717827?ie=UTF8&qid=1516474531&sr=8-1-fkmr0&keywords=Adobe+65270553BA03A12+13
2. https://www.amazon.com/CALIDAD-Metodolog%C3%ADa-aplicaciones-Ejercicios-resueltos/dp/1491223286/ref=sr_1_fkmr0_1/143-1437888-1275633?ie=UTF8&qid=1516474761&sr=8-1-fkmr0&keywords=CON+SAS+95298200
3. https://www.amazon.com/Text-Messages-Gone-Wrong-Funny-ebook/dp/B00UGHV0PG/ref=sr_1_fkmr0_1/143-7262426-0060317?ie=UTF8&qid=1516474763&sr=8-1-fkmr0&keywords=CON+SSSNP+SMS+1
4. https://www.amazon.com/Delphi-Resistance-Trilogy/dp/1542047226/ref=sr_1_fkmr0_1/138-8927465-1388612?ie=UTF8&qid=1516474843&sr=8-1-fkmr0&keywords=Delphi+DFG0008
5. https://www.amazon.com/Microsoft-Windows-Small-Business-Server/dp/3866451261/ref=sr_1_fkmr0_1/137-1878444-6191143?ie=UTF8&qid=1516475239&sr=8-1-fkmr0&keywords=Microsoft+126+00159+3
6. https://www.amazon.com/Sweet-Land-Liberty-Deborah-Hopkinson/dp/1561453951/ref=sr_1_1/137-4801123-6346234?ie=UTF8&qid=1516475317&sr=8-1&keywords=Peachtree+null
7. https://www.amazon.com/ORIGINAL-APPLICATION-PREVENTING-MIS-CUEING-BILLIARDS/dp/B000HHN1JS/ref=sr_1_1/136-0514910-0758544?ie=UTF8&qid=1516475402&sr=8-1&keywords=Rare+20453
8. https://www.amazon.com/SolarWinds-Orion-Network-Performance-Monitor/dp/1849688486/ref=sr_1_fkmr0_1/137-5341905-1256363?ie=UTF8&qid=1516475532&sr=8-1-fkmr0&keywords=SolarWinds+3054

### "Available from these sellers"

1. https://www.amazon.com/Healthline-Folding-Aluminum-Rollator-Lightweight/dp/B0753C2NHB/ref=sr_1_fkmr0_1_a_it/130-5613996-7927757?ie=UTF8&qid=1516474386&sr=8-1-fkmr0&keywords=24%22W+Black%2FBlue+Plastic+3+Piece+Handle+Sweep+Complete+Broom+w%2FSqueegee
2. https://www.amazon.com/Duracell-Coppertop-Alkaline-Batteries-Doublewide/dp/B000FD6RTA/ref=sr_1_1_a_it/146-3829409-1091328?ie=UTF8&qid=1516474879&sr=8-1&keywords=Duracell+MN14RT8Z

### "Sale price"

1. https://www.amazon.com/UltraSofts-Sailor-Top-Azalea-Medium/dp/B00CEEJXVM/ref=sr_1_fkmr0_1/142-4494024-3253816?ie=UTF8&qid=1516474451&sr=8-1-fkmr0&keywords=15454+M+CBL+L+IND
2. https://www.amazon.com/Layered-Dresses-Christening-Birthday-Occasion/dp/B075GXHYFD/ref=sr_1_fkmr0_1/139-0520420-9970857?ie=UTF8&qid=1516475730&sr=8-1-fkmr0&keywords=XTRCMSSM+M+02


### It's a movie (type 1)

1. https://www.amazon.com/Armstrong-Lie-Lance/dp/B00GMV8DFU/ref=sr_1_1/145-2853230-7481957?ie=UTF8&qid=1516474553&sr=8-1&keywords=Armstrong+null

### It's a movie (type 2)

1. https://www.amazon.com/I-Tonya-Margot-Robbie/dp/B078944PGN/ref=sr_1_fkmr0_1/143-8082553-8208156?ie=UTF8&qid=1516475377&sr=8-1-fkmr0&keywords=RPS16DC+I

### It's a music CD

1. https://www.amazon.com/Colors-Explicit-Beck/dp/B074X1FFZ1/ref=sr_1_fkmr0_1/143-1828333-6030567?ie=UTF8&qid=1516474618&sr=8-1-fkmr0&keywords=BECK+330043407

### Standard product page

1. https://www.amazon.com/SAF3275BL-Safco-Onyx-Hospitality-Organizer/dp/B00N3BDZ46/ref=sr_1_1/139-1952273-7032932?ie=UTF8&qid=1516475435&sr=8-1&keywords=SAF3275BL

### "Temporarily out of stock"

1. https://www.amazon.com/TownSteel-FME-4000-Frequency-Instantly/dp/B00YM75SJK/ref=sr_1_fkmr0_1/143-9413147-6558936?ie=UTF8&qid=1516475587&sr=8-1-fkmr0&keywords=TOWNSTEEL+FME+2030+RFID+G+626


## What should be scraped

## 1 AZO

{
	"_id": "azo",
	"startUrl": [
		"http://weiksner.com/amzn/azo.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "sku",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "div.grid-19 h3.simple",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "part_no",
			"selector": "span.part-number span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "td.price span:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "in_stock",
			"selector": "div.button-bar-msg-in-stock",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "cat1",
			"selector": "ul.inline.breadcrumb li:nth-of-type(2) a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "cat2",
			"selector": "ul.inline.breadcrumb li:nth-of-type(3) a",
			"delay": ""
		}
	]
}
## 2 BUNZL

{
	"_id": "bunzl",
	"startUrl": [
		"http://weiksner.com/amzn/scrape/bunzl/index.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "search",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"search"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "results",
			"selector": "div.product-details",
			"delay": ""
		},
		{
			"parentSelectors": [
				"results"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "product",
			"selector": "a.product-name",
			"delay": ""
		},
		{
			"parentSelectors": [
				"results"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "min price",
			"selector": "a.minimal-price-link span.price",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"results"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "regular price",
			"selector": "span.regular-price span.price",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "item #",
			"selector": "p.product-ids",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "shipping",
			"selector": "p.availability span",
			"regex": "",
			"delay": ""
		}
	]
}

## 3 CDW

{
	"_id": "cdw-tech",
	"startUrl": [
		"http://weiksner.com/amzn/techdist/cdw.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple":s false,
			"id": "sku",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(4)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "product-link",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "span.fn",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "div.productRight span.selected-price span:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfg #",
			"selector": "span.mpn",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "cdw #",
			"selector": "span.part-number:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "ship",
			"selector": "div.short-message-block span.message",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "ship2",
			"selector": "div.long-message-block span.message",
			"regex": "",
			"delay": ""
		}
	]
}

## 4 CNXN

{
	"_id": "cnxn",
	"startUrl": [
		"http://weiksner.com/amzn/techdist/cnxn.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "sku",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(4)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "product-link",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "h1.pagetitle",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "brand",
			"selector": "div.col-xs-12 div.col-lg-12 a",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "cnxn #",
			"selector": "span#productSku",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfg #",
			"selector": "span#productManufacturerPartNumber",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "ship",
			"selector": "span#productEstimatedShipping",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "span.priceDisplay",
			"regex": "",
			"delay": ""
		}
	]
}

## 5 FAST

{
	"startUrl": [
		"http://weiksner.com/amzn/price/fast.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "sku",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "div.info--description",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "div.whole__sale--label",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "brand",
			"selector": "div.general-info--value span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "fast part no",
			"selector": "tr:contains('Fastenal Part No. (SKU)') div.general-info--value",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "unspsc",
			"selector": "a.popup",
			"regex": "",
			"delay": ""
		}
	],
	"_id": "fast-price"
}

## 6 GWW

{
	"selectors": [
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "h1.productName",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "span.gcprice-value",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "per",
			"selector": "span.gcprice-unit",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "shipping",
			"selector": "span.rta-message-confirmation",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "item_id",
			"selector": "div.head-container li:nth-of-type(1) span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfr_id",
			"selector": "div.head-container li:nth-of-type(2) span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "unspsc",
			"selector": "li#unspc span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "brand",
			"selector": "a.brand",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "drop ship",
			"selector": "span.rta-message-error",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "sku",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "get-this-price",
			"selector": "div.gcprice p.gcprice span:nth-of-type(2)",
			"regex": "",
			"delay": ""
		}
	],
	"startUrl": [
		"http://weiksner.com/amzn/grainger200.php"
	],
	"_id": "grainger-200"
}

## 7 HDSS

{
	"startUrl": [
		"http://weiksner.com/amzn/hdss.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "sku",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "h1.space-bottom",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "instock",
			"selector": "div.form-inline div strong",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "unspsc",
			"selector": "tr:contains('UNSPSC') td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "brand",
			"selector": "tr:contains('Brand') td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "part-no",
			"selector": "tr:contains('Manufacturer Part Number') td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "Shipping details",
			"selector": "div.span7 div.well",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "price-tier",
			"selector": "li div.row-fluid",
			"delay": ""
		},
		{
			"parentSelectors": [
				"price-tier"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "quantity",
			"selector": "div.span5",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"price-tier"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "priceq",
			"selector": "div.span7",
			"regex": "",
			"delay": ""
		}
	],
	"_id": "hdss"
}

## 8 NSIT

{
	"startUrl": [
		"http://weiksner.com/amzn/techdist/nsit.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "sku",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(4)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "product-link",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "h1 a",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfg #",
			"selector": "div.prod-description-bottom td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "insight #",
			"selector": "div.prod-description-bottom td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "avail",
			"selector": "p.prod-stock span.js-prod-available",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "instock",
			"selector": "p.prod-stock",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "div.columns p.prod-price",
			"regex": "",
			"delay": ""
		}
	],
	"_id": "nsit"
}

## 9 TECD

{
	"startUrl": [
		"http://weiksner.com/amzn/techdist/tecd.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "sku",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(4)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "product-link",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "a.productDetailsLink",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "msrp",
			"selector": "div.priceDisplay span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfr #",
			"selector": "div.productCodes div:nth-of-type(2) span.darkTxt",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "tecd #",
			"selector": "div.productCodes div:nth-of-type(1) span.darkTxt",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "status",
			"selector": "div.StatusMSRPavail",
			"regex": "",
			"delay": ""
		}
	],
	"_id": "tecd-tech"
}

## 10 PMCI

{
	"startUrl": [
		"http://weiksner.com/amzn/techdist/tecd.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "sku",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(4)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "product-link",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "a.productDetailsLink",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "msrp",
			"selector": "div.priceDisplay span",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfr #",
			"selector": "div.productCodes div:nth-of-type(2) span.darkTxt",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "tecd #",
			"selector": "div.productCodes div:nth-of-type(1) span.darkTxt",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"product-link"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "status",
			"selector": "div.StatusMSRPavail",
			"regex": "",
			"delay": ""
		}
	],
	"_id": "tecd-tech"
}

## 11 Zoro

{
	"selectors": [
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "in_stock",
			"selector": "span.avl-in-stock",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "product",
			"selector": "h1.productName",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "h3.main-heading-font span:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "zoro_id",
			"selector": "div.brand span:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfr_id",
			"selector": "span:nth-of-type(4)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "shipping time",
			"selector": "div.ships-from-lead-time",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "sku",
			"selector": "a",
			"delay": ""
		}
	],
	"startUrl": [
		"http://weiksner.com/amzn/zoro.php"
	],
	"_id": "zoro-all"
}

## 12 MSM

{
	"_id": "msm-sample",
	"startUrl": [
		"http://weiksner.com/amzn/msm-sample.php"
	],
	"selectors": [
		{
			"parentSelectors": [
				"_root"
			],
			"type": "SelectorElement",
			"multiple": true,
			"id": "table",
			"selector": "table",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "sku",
			"selector": "a",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "date",
			"selector": "td:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"table"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "site",
			"selector": "td:nth-of-type(1)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorLink",
			"multiple": false,
			"id": "Product",
			"selector": "h1",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "brand",
			"selector": "div.col-xs-4 div.pdp-spec-row:nth-of-type(3) div.pdp-spec-value",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "msc part #",
			"selector": "div.col-xs-4 div.pdp-spec-row:nth-of-type(4) div.pdp-spec-value",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "upc #",
			"selector": "div.pdp-spec-row:nth-of-type(5) div.pdp-spec-value",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "cat 1",
			"selector": "div.row div.row div.col-xs-9 a:nth-of-type(2)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "cat 2",
			"selector": "div.col-xs-9 a:nth-of-type(3)",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "price",
			"selector": "span.atc-pdpPrice",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "in stock",
			"selector": "div.pdp-stock strong",
			"regex": "",
			"delay": ""
		},
		{
			"parentSelectors": [
				"sku"
			],
			"type": "SelectorText",
			"multiple": false,
			"id": "mfr #",
			"selector": "div.col-xs-4 div.pdp-spec-row:nth-of-type(5) div.pdp-spec-value",
			"regex": "",
			"delay": ""
		}
	]
}
