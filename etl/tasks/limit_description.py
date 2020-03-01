MAX_CHARACTERS = 200


def limit_description(item: dict):
    if 'description' not in item:
        return item

    if (len(item['description']) > MAX_CHARACTERS):
        ellipsis = '...'
        maxCharacters = MAX_CHARACTERS - len(ellipsis)
        item['description'] = item['description'][:maxCharacters] + ellipsis

    return item
