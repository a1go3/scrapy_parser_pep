from pathlib import Path
import csv
from collections import defaultdict
from datetime import datetime
from .utils import get_result_pep, file_output

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILENAME = 'status_summary_{time}.csv'



class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.total = len(item['status'])
        if item['status'] is not None:
            self.results[item['status']] += 1
        else:
            self.results['Draft'] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / FILENAME.format(
            time=datetime.now().strftime(DATETIME_FORMAT))
        with open(file_path, mode='w',
                  encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            writer.writerows(
                [['Статус', 'Количество'],
                 *(self.results.items()),
                 ['Total', sum(self.results.values())]
                 ])



# class PepParsePipeline:
#
#     def open_spider(self, spider):
#         self.statuses = defaultdict(lambda: 0)
#
#     def process_item(self, item, spider):
#         status = item['status']
#         self.statuses[status] += 1
#         return item
#
#     def close_spider(self, spider):
#         results = [('Статус', 'Количество')]
#         results.extend(self.statuses.items())
#         total = sum(self.statuses.values())
#         results.append(('Total', total))
#         time = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         file_path = BASE_DIR / f'results/status_summary_{time}.csv'
#         with open(file_path, 'w', encoding='utf-8') as file:
#             csv_writer = csv.writer(file, dialect='unix')
#             csv_writer.writerows(results)