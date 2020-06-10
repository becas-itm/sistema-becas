from etl.common.entities import get_entity_full_name


def add_entity_fields(item: dict):
    code = item['spider']['name']

    item['entity'] = {
        'code': code,
        'name': get_entity_full_name(code),
    }

    return item
