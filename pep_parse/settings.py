from datetime import datetime
from pathlib import Path


BOT_NAME = "pep_parse"
SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

NAME = 'pep'
ALLOWED_DOMAINS = 'peps.python.org'
START_URLS = 'https://peps.python.org/'

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TIME = datetime.now().strftime(DATETIME_FORMAT)
FILE_NAME = f'status_summary_{TIME}.csv'

ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}