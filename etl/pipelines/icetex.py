import bonobo

from scraper.spiders import SpiderName
from etl.common.date_parser import ISO_FORMAT
from itm.documents import connect_db

from etl.tasks.icetex import calculate_academic_level
from etl.tasks.icetex.extract_country import extract_country
from etl.tasks import read_raw_scholarhips, \
    add_timestamps, \
    add_pending_state, \
    add_entity_full_name, \
    limit_description, \
    parse_deadline, \
    save_scholarship, \
    parse_funding_type


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(read_raw_scholarhips(SpiderName.ICETEX),
                    parse_deadline(ISO_FORMAT),
                    add_timestamps,
                    add_pending_state,
                    limit_description,
                    calculate_academic_level,
                    extract_country,
                    add_entity_full_name,
                    parse_funding_type,
                    save_scholarship)
    return graph


def get_services(**options):
    return {}


if __name__ == '__main__':
    connect_db()
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(get_graph(**options), services=get_services(**options))
