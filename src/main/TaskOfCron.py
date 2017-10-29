import os
import yaml
import urllib2
from apscheduler.schedulers.blocking import BlockingScheduler

DEFAULT_PATH = "../resources/"


def job():
    print "hello this is the first job!!!!"


def readYaml():
    configDict = {}
    filenames = os.listdir(DEFAULT_PATH)
    for file in filenames:
        configDict = yaml.load(open(DEFAULT_PATH + "/" + file))
        print configDict
    return configDict


if __name__ == '__main__':
    print readYaml()
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', second=readYaml()['pl-a-batch'], hour='*')
    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
