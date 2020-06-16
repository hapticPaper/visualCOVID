from apscheduler.schedulers.blocking import BlockingScheduler
import os, requests, datetime
from sqlalchemy import create_engine
from frontend.db_loader.lite_loader import *
import logging as l

DB_PATH = '../data/db/'
DB_FILE = 'covid.sqlite'
os.makedirs(DB_PATH, exist_ok=True)
ENG = create_engine(f'sqlite:///{os.path.join(DB_PATH, DB_FILE)}')


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=2)
def updateSqlite():
    results = fetchCovidData(ENG)
    l.info(f'results: {results[:2]}')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')
sched.start()