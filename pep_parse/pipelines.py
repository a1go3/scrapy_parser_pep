from collections import defaultdict
from itemadapter import ItemAdapter
from pathlib import Path

from .utils import get_result_pep, file_output

BASE_DIR = Path(__file__).parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    counts = defaultdict(int)

    def open_spider(self, spider):
        ...

    def process_item(self, item, spider):

        # counts = defaultdict(int)

        # adapter = ItemAdapter(item)
        status = item['status']
        # status = adapter.get('status')
        self.counts[status] += 1
        result = get_result_pep(self.counts)
        file_output(result)
        return item

    def close_spider(self, spider):
        # result = get_result_pep(self.counts)
        # return file_output(result)
        pass