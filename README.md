
# Product Scraper

- Omar Trejo
- January, 2018

## Setup and Execute in Ubuntu 16 Environment

- TODO

## Tasks

### Day 1

| Status  | Task                                                        | Note                                 |
|---------|-------------------------------------------------------------|--------------------------------------|
| Done    | Join site and spreadsheet search strings                    |                                      |
| Done    | Test CSS selectors from `amzn` file                         |                                      |
| Done    | Removed 1,240 duplicates between site and spreaddsheet data |                                      |
| Done    | General search capability search-to-new-results-page        |                                      |
| Done    | Test general search capability for Amazon                   |                                      |
| Done    | Use first-result mechanim to retrieve relevant item         |                                      |
| Pending | Environment installlation scripts for Ubuntu 16             | Must be tested at least once by Mike |

### Day 2

| Status      | Task                                                 | Note                             |
|-------------|------------------------------------------------------|----------------------------------|
| Done        | Fix Twisted Reactor bug when scraping multiple sites |                                  |
| Done        | Test with two sites at the same time (use Staples)   |                                  |
| Done        | Initial throttling mechanism                         |                                  |
| Done        | Initial randomized proxy mechanism                   |                                  |
| Done        | Initial randomize user-agent mechanism               |                                  |
| Done        | Resarch best way to save results into database       | Best done using `Item Pipelines` |
| In Progress | Save information for unhandled requests              |                                  |
| In Progress | Update documentation                                 |                                  |

### Day 3

| Status       | Task                              | Note                     |
|--------------|-----------------------------------|--------------------------|
| To be agreed | Save results into database        | Which database?          |
| To be agreed | Retrive fresh proxy list from API | Must be US based proxies |
