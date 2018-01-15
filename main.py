
# from utilities.scheduler import Scheduler
from settings import SETTINGS
from sites.site import Site

SITES = [
    Site('Amazon', SETTINGS)
    # Other sites go here...
]


def main():
    print("[+] Ready...")
    for site in SITES:
        site.scrape()

    # When implementing scheduled scraping, this code will
    # come in handy. The implementation is practically
    # finished, but I still need to test it, and I did
    # not have time to do it for this time.
    #
    # scheduler = Scheduler().get_scheduler()
    # for site in SITES:
    #     scheduler.add_job(
    #         site.scrape(async=True),
    #         "cron", hour="*/1", timezone="America/Mexico_City")
    # scheduler.start()


if __name__ == "__main__":
    main()
