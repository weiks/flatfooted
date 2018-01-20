
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

- [X] Join site and spreadsheet search strings
- [X] Test CSS selectors from `amzn` file
- [X] Removed 1,240 duplicates between site and spreaddsheet data
- [X] General search capability search-to-new-results-page
- [X] Test general search capability for Amazon
- [X] Use first-result mechanim to retrieve relevant item
- [ ] Environment installlation scripts for Ubuntu 16
  - Must be tested at least once by Mike

### Phase 2

- [X] Fix Twisted Reactor bug when scraping multiple sites
- [X] Test with two sites at the same time (use Staples)
- [X] Initial throttling mechanism
- [X] Initial randomized proxy mechanism
- [X] Initial randomize user-agent mechanism
- [X] Resarch best way to save results into database
  - Best done with `Item Pipelines`
- [X] Handle 429 (and possibly) other response codes
- [X] Include `search_string` to correlate results
- [X] Save information for unhandled requests
- [X] Update documentation
- [X] Remove non-ASCII characters that affect data post-processing
- [X] Retrieve fresh proxy list from API
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

- [ ] Save raw HTML to re-scrape it if necessary without re-crawling
- [ ] Look errors in the request-response cycle (3 out of 322 missing searches
  for Amazon)
  - Compare input/output differences to detect these cases

## Current Status

Two tests are being executed right now. I'm running the scrapper in the Amazon
instance provided (using `tmux`), to test the difference in results between
using and not using proxies. I'm looking for differences in execution time and
actual data scraped.

The tests were started around 4:30 AM (CDT). The earlier one uses proxies, while
the latter one doesn't. I'm mentioning this in case Mike decides to run more
processes and we don't get confused with the data files.

IMPORTANT: Mike, please don't use the `tmux` sessions, as I need those to verify
the time taken for each test.
