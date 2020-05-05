import bonobo

from itm.documents import connect_db

from etl.common.entities import EntityName

from etl.tasks import read_raw_scholarhips, \
    add_timestamps, \
    add_pending_state, \
    add_entity_fields, \
    limit_description, \
    save_scholarship, \
    capitalize_name, \
    calc_fill_status

from etl.tasks.daad import calculate_academic_level


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(read_raw_scholarhips(EntityName.DAAD),
                    add_timestamps,
                    add_pending_state,
                    capitalize_name,
                    limit_description,
                    add_entity_fields,
                    calculate_academic_level,
                    calc_fill_status,
                    save_scholarship)
    return graph


def get_services(**options):
    return {}


if __name__ == '__main__':
    connect_db()
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(get_graph(**options), services=get_services(**options))
