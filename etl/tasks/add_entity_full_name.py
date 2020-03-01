from scraper.spiders import SpiderName


ENTITIES_FULL_NAME_BY_SPIDER = {
    SpiderName.ICETEX: 'ICETEX',
    SpiderName.DAAD: 'Servicio Alemán de Intercambio Académico',
}


def add_entity_full_name(item: dict):
    spider = SpiderName(item['spider']['name'])
    fullName = ENTITIES_FULL_NAME_BY_SPIDER.get(spider)

    if 'entity' in item:
        item['entity']['fullName'] = fullName
    else:
        item['entity'] = dict(fullName=fullName)

    return item
