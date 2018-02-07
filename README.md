
# Item Scraper

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

- `save_html` (`True`/`False`): whether to save HTML files for crawled pages.
- `random_proxies` (`True`/`False`): use a random proxy for each request.
- `random_user_agents` (`True`/`False`): use a random User Agent for each
  request.
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
- `sites` (dictionary): specification for the data to be scraped from each site
  with the following structure:
  - `site_name` (dictionary):
    - `base_url` (string): URL used to fix relative URLs within crawled pages.
    - `search` (dictionary): specification for search parameters for site.
      - `query` (string): URL used for searching (with `{}` where search strings
        should appear).
      - `auto_redirected` (list of strings, optional): if specified, a site's
        search pages will pass through a "auto-redirected detector" which uses
        the specified XPATH/CSS selectors to detect whether the return page is
        an "item page" insteado of a "search page", and if it is, it will be
        treated as such. The selectors I'm using for now look for price data for
        this detection mechanism.
      - `double_hop` (list of strings, optional): if specified, a site's search
        pages will pass through a "double hop detector" which uses the specified
        XPATH/CSS selectors to detect whether a page is a "intermediate" hop. If
        such detection is positive, the first category will be passed through to
        the standard "search page" parser, otherwise, it will be treated as a
        "search page" itself.
      - `first_item` (list of strings): XPATHs used to identify the first item
      - `fields` (dictionary): where each key is a string with the name of the
        variable as it will be store in the CSV (may end with `_css` to indicate
        that a CSS selector should be used instead of an XPATH selector), and
        the value should be a list with strings representing XPATH/CSS
        selectors.
    - `item` (dictionary, optional): specification for item parameters for site.
      - `fields` (dictionary): same as the `fields` dicitonary for `search`.

### Execute

Once the `settings.py` have been adjusted, execute:

```
$ python3 main.py
```

The results will be in the `outputs/` directory.

If we want to both save a log with the output as well as see the actual output
in real-time in the terminal, we can use the following instead (you may use the
`.txt` extension instead of `.log` if you prefer):

```
$ python3 -u main.py | tee outputs/log.txt
```

If we want to execute under a schedule, we can use the native `cron` utility for
Ubuntu. First we need to edit `crontab` entries using the following command:

```
$ sudo crontab -e
```

Inside that file, we can use of the following specifications:

```
# Every minute
*/1 * * * * python3 -u /path/to/main.py | tee "/path/to/outputs/log_$(date +\%Y-\%m-\%d).txt"

# Every hour (sharp)
0 * * * * python3 -u /path/to/main.py | tee "/path/to/outputs/log_$(date +\%Y-\%m-\%d).txt"

# Every day (midnight)
0 0 * * * python3 -u /path/to/main.py | tee "/path/to/outputs/log_$(date +\%Y-\%m-\%d).txt"

# Every week (Sunday midnight)
0 0 0 * * python3 -u /path/to/main.py | tee "/path/to/outputs/log_$(date +\%Y-\%m-\%d).txt"
```

After saving the file, `cron` will start executing these jobs (look for the
`log.txt` to verify the job ran when you expected it to). You can also see the
list of current `cron` jobs with:

```
$ sudo crontab -l
```

## Tasks

### Phase 1

- [x] Join site and spreadsheet search strings
- [x] Test CSS selectors from `amzn` file
- [x] Removed 1,240 duplicates between site and spreaddsheet data
- [x] General search capability search-to-new-results-page
- [x] Test general search capability for Amazon
- [x] Use first-result mechanim to retrieve relevant item
- [x] Environment installlation scripts for Ubuntu 16

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
  - When comparing number of lines in input file vs number of items in
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
    well as the information for the corresponding items.

### Phase 4

- [x] Insert metadata (`site_name` and `timestamp`) into results
- [x] Keep track of "0 results" in the Amazon data
- [x] JOIN by `search_string` in post-processing script
  - Need to separate URLs into "search URL" and "item URL", as well as
    HTTP status codes for searches and items
- [x] Deal with JavaScript enabled sites by using headless browser
  - Currently there's a manual process to specify what should be looked for to
    detect that a site has finshed loading the data we need. This is necessary
    because some sites take a bit longer. Should these be specified through the
    settings file?
- [ ] Get indicator for "suggeted" results or "no results" for a search
  - [x] Zoro (`ZORO`): **DONE** (No "suggested" results indicator)
  - [x] Grainger (`GWW`): **DONE**
  - [x] CDW (`CDW`): **DONE**
  - [x] Connection (`CNXN`): **DONE**
  - [x] TechData (`TECD`): **DONE**
  - [x] Insight (`NSIT`): **DONE**
  - [x] Fastenal (`FAST`): **DONE** (No "suggested" results indicator)
  - [x] AutoZone (`AZO`): **DONE** (No "suggested" results indicator)
  - [ ] Bunzlpd (`BUNZL`): Pending decision by Mike (OR/AND issue)
  - [x] Tiger Direct (`PCMI`): **DONE**
  - [x] MSC Direct (`MSM`): **DONE**
  - [x] HD Supply Solutions (`HDSS`): **DONE**
  - [ ] Biggest Book (`ESND`): Pending fragmented URLs
  - [x] Staples (`STAPLES`): **DONE**

### Phase 5

- [x] Optionally retrieve item data directly from results page
  - I changed things so that if the `item` key is ommitted from the settings for
    a site, then it means that only results from the search page will be used,
    and the item data should be specified in its corresponding `fields`.
- [x] Optionally specify that an auto-redirect into item is expected
- [x] Optionally specify when double-hops should be used
- [ ] Make sure we can reliably scrape Amazon and Zoro
- [x] Make proxies work together with Selenium
  - [ ] TODO: Waiting for Mike to whitelist new instance's IP for proxies
- [x] Save into a relational database (single table)
  - [x] Save each page as it's scraped
  - [ ] Easily etrieve saved HTML
- [x] Setup periodic scraping for once a day
- [ ] Deterministic column order in CSVs (delete?)

## Site Groups

#### Group 1

- [x] `ZORO` https://www.zoro.com/search?q=pen
  - Status: **DONE**
  - JavaScript: Yes
  - Auto-rediret: Yes
  - Use search page: No
  - Double-hop: No
  - Uses automatic redirects (302) when a unique item was found (I guess):
    - Example, search for: QUA41967
      - In: https://httpstatus.io/
      - Use: https://www.zoro.com/search?q=QUA41967
- [x] `GWW` https://www.grainger.com/search?searchQuery=pen
  - Status: **DONE**
  - JavaScript: Yes
  - Auto-redirect: Yes
  - Use search page: No
  - Double-hop: No
  - Seems that JavaScript is required to actually interact with the site and get
    the data we are looking for. This can be a bit tricky, but will explore it
    later.
    - As suggested by Mike, the JavaScript interaction may be bypassed if we are
      able to use an identifier from the `Zoro` data, and use that as the search
      string. This will bypass a "results page" and go straight to "item page".
    - This is how we solved it. However, this requires a "special" search
      strings list that contains the `MFR` IDs for the items. Any other search
      may produce results, but currently we are not able to crawl them.

#### Group 2

- [x] `CDW` https://www.cdw.com/search/?key=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: Yes
  - Use search page: No
  - Double-hop: No
- [x] `CNXN` https://www.connection.com/IPA/Shop/Product/Search?term=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: Yes
  - Use search page: No
  - Double-hop: No
  - I'm getting a lot of 404 (Not Found) and 302 (Moved)
    - It seems that when an item is not found, they return a 404 instead of
      simply returning a 200. They are using HTML status code incorrectly. It
      doesn't affect functionality, but leaves 404's in the spreadsheet instead
      of leaving a 200 with a "research without results" indicator. Should we
      fix this?
    - When a result is actually returned (maybe when it's the only one), we're
      automatically redirected to the item page (with a 302), and that is
      messing up the mechanism. Need to look into this further. This definitely
      needs to be fixed.
    - Working around the misuse of the HTTP response codes can be very tricky,
      and it won't add value to the analysis. I propose that we deal with it in
      the post-processing, and leave as is for now.
- [x] `TECD` https://shop.techdata.com/searchall?kw=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: No
  - Use search page: Yes
  - Double-hop: No
  - "Item page" needs sign-in account
- [x] `NSIT` https://www.insight.com/en_US/search.html?q=pen
  - Status: **DONE**
  - JavaScript: Yes
  - Auto-redirect: Yes
  - Use search page: No
  - Double-hop: No
  - Sometimes price is held back behind a "Estimate the total price of this
    item" button. However, it's not working because even if we put a valid ZIP
    code, the price comes as "$0", and we need to call their number to get a
    price. These cases will be marked as not having a price. Other cases, were
    price does appear, just proceed normally.

#### Group 3

- [x] `FAST` https://www.fastenal.com/products?term=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: No
  - Use search page: No
  - Double-hop: No
  - There are no identifiers in the first/main table, so the fields can move
    around without ourselves knowing apriori where they will be. We need some
    kind of dynamic parsing for this (check each field until we find the word
    "Manufacturer" in one of the cells, and use the appropriate value)
    - How to proceed: save all the data in the table as a single string.
- [ ] `AZO` https://www.autozone.com/searchresult?searchText=pen
  - Status: Defered (double-hop and ZIP)
  - JavaScript: No
  - Auto-redirect: No
  - Use search page: No
  - Double-hop: Yes
  - Asks for ZIP

#### Group 4

- [x] `BUNZL` https://www.bunzlpd.com/catalogsearch/result/?q=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: No
  - Use search page: No
  - Double-hop: No
- [x] `PCMI` http://www.tigerdirect.com/applications/SearchTools/search.asp?keywords=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: No
  - Use search page: No
  - Double-hop: No
- [x] `MSM` https://www.mscdirect.com/browse/tn/?searchterm=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: Yes
  - Use search page: No
  - Double-hop: Yes
  - How to proceed (by Mike):
    - If it goes to "categories" mark it as not having results
    - If it goes to "search results" proceed normally
    - If it auto-redirects to item, proceed normally
  - I was able to go through "categories" pages to follow through the double
    hop, which is more than what Mike asked for and allows us to get more item
    data.
- [x] `HDSS` https://hdsupplysolutions.com/shop/SearchDisplay?searchTerm=pen
  - Status: **DONE**
  - JavaScript: No
  - Auto-redirect: No
  - Use search page: No
  - Double-hop: No
  - Sometimes `instock` button requires site account for checking
- [ ] `ESND` http://biggestbook.com/ui/catalog.html#/search?keyword=pen
  - Status: Defered (framgmented URLs)
  - JavaScript: Yes
  - Auto-redirect: Yes
  - Use search page: No
  - Double-hop: No
  - This site has fragmented URLs, meaning that they contain a `#` character,
    which is used to identify sections within a page, not a different, page,
    and that's causing problems with Scrapy and Selenium. Need to look into
    this further.
- [x] `STAPLES` https://www.staples.com/{0}/directory_{0}?
  - Status: **DONE**
  - JavaScript: Yes
  - Auto-redirect: No
  - Use search page: No
  - Double-hop: No
  - Note that the search URL is dynamic in the sense that it needs the field to
    be filled twice in different places.
  - The site gives problematic results when a `?` character is used in the
    search, probably due to the dynamic nature of the URL and the fact that the
    `?` symbol is used to specify parameters in a URL. These should be avoided
    in the search strings.

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
|               1 | Standard item page             | Yes          | Extra XPATH                                                                                     | ?          | Should've been scraped            |
