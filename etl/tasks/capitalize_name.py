from etl.common.casing import case_title


def capitalize_name(item):
    if 'name' not in item or 'language' not in item:
        return item

    item['name'] = case_title(item['name'], item['language'])

    return item
