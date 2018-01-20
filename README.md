
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
- [ ] Re-test 7 failed search cases with 2 new XPATHs for Amazon

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
|               1 | Standard product page          | Yes          | Extra XPATH                                                                                     | ?          |                                   |

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
