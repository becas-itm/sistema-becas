from etl.common.date_parser import DateParser


def parse_deadline(dateformat: str):
  parser = DateParser(dateformat)

  def run_task(item: dict):
    if 'deadline' in item:
      item['deadline'] = parser(item['deadline'])

    return item

  return run_task
