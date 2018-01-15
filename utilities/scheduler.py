
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor


class Scheduler:

    JOB_DEFAULTS = {'coalesce': True, 'max_instances': 4}
    EXECUTORS = {'default': ThreadPoolExecutor(30)}

    def __init__(self, group):
        jobs_database = 'sqlite:///jobs_' + str(group) + '.sqlite'
        self.JOB_STORES = {'default': SQLAlchemyJobStore(url=jobs_database)}

    def get_scheduler(self):
        return BlockingScheduler(
            jobstores=self.JOB_STORES,
            executors=self.EXECUTORS,
            job_defaults=self.JOB_DEFAULTS
        )
