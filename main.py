
# from utilities.scheduler import Scheduler
from scraper.scraper import Scraper
from settings import SETTINGS


def main():
    print("[+] Ready...")
    scraper = Scraper(SETTINGS)
    scraper.start()
    scraper.json_to_csv()

    # When implementing scheduled scraping, this code will
    # come in handy. The implementation is practically
    # finished, but I still need to test it, and I did
    # not have time to do it for this time.
    #
    # scheduler = Scheduler().get_scheduler()
    # for site in SITES:
    #     scheduler.add_job(
    #         site.scrape(async=True),
    #         "cron", day="*/1", timezone="America/Mexico_City")
    # scheduler.start()


if __name__ == "__main__":
    main()
