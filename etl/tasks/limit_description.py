import spacy


from etl.common import Language

es_nlp: spacy.tokens.Doc = spacy.load('es_core_news_sm')
en_nlp = spacy.load('en_core_web_sm')


def limit_description(item: dict):
    if 'description' not in item or 'language' not in item:
        return item

    item['description'] = extract_first_sentence(item['description'], item['language'])

    return item


def extract_first_sentence(text, language):
    language = Language(language)

    doc = None
    if language == Language.SPANISH:
        doc = es_nlp(text)
    elif language == Language.ENGLISH:
        doc = en_nlp(text)

    return str(list(doc.sents)[0]) if doc else text
