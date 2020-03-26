from etl.common.entities import get_entity_full_name


def add_entity_fields(item: dict):
    name = item['spider']['name']

    item['entity'] = {
        'name': name,
        'fullName': get_entity_full_name(name),
    }

    return item
