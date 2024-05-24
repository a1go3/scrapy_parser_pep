import csv
from collections import defaultdict

from .settings import BASE_DIR, FILE_NAME


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):

        file_path = self.results_dir / FILE_NAME

        with open(file_path, mode='w',
                  encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            writer.writerows(
                [['Статус', 'Количество'],
                 *(self.results.items()),
                 ['Total', sum(self.results.values())]
                 ])
