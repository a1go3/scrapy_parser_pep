
from pathlib import Path
import csv
import datetime as dt

BASE_DIR = Path(__file__).parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'



def get_result_pep(counts):
    """Формирует итоговый список функции pep."""
    all_peps = 0
    results = [('Статус', 'Количество'), ]
    for key, value in counts.items():
        all_peps += value
        list_new = [key, value]
        results.append(tuple(list_new))
    results.append(('Total', all_peps))
    return results


def file_output(results, cli_args):
    """Вывод результата работы функции в .csv файл."""
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'pepstatus_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)