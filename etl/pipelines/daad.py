import bonobo

from scraper.spiders import SpiderName
from itm.documents import connect_db

from etl.tasks import read_raw_scholarhips, \
    add_timestamps, \
    add_pending_state, \
    add_entity_full_name, \
    limit_description, \
    save_scholarship


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(read_raw_scholarhips(SpiderName.DAAD),
                    add_timestamps,
                    add_pending_state,
                    limit_description,
                    add_entity_full_name,
                    save_scholarship)
    return graph


def get_services(**options):
    return {}


if __name__ == '__main__':
    connect_db()
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(get_graph(**options), services=get_services(**options))
