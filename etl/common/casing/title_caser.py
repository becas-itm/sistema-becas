import spacy

from etl.common import Language


es_nlp = spacy.load('es_core_news_md')
en_nlp = spacy.load('en_core_web_md')


def case_title(text, language):
    language = Language(language)

    if language == Language.SPANISH:
        return case_title_apa_spanish_rules(text)

    if language == Language.ENGLISH:
        return case_title_apa_english_rules(text)

    return text


def case_title_apa_spanish_rules(text):
    def should_capitalize(token):
        return token.pos_ in ['NN', 'NNS', 'PROPN']

    tokens = []
    for token in es_nlp(text.lower()):
        if should_capitalize(token) or is_first(token):
            tokens.append(token.text.capitalize())
        else:
            tokens.append(token.text)

    return ' '.join(tokens)


def case_title_apa_english_rules(text):
    title = ''
    for token in en_nlp(text):
        if (
            len(token) >= 4 or
            is_first(token) or
            token.tag_ == 'PRP' or
            next_token(token).tag_ == 'HYPH'
        ):
            title += token.text.capitalize()
        else:
            title += token.text.lower()

        if not next_token(token).is_punct and token.tag_ != 'HYPH':
            title += ' '

    return title


def is_first(token):
    return token.i == 0


def next_token(token):
    return token.doc[token.i + 1] if has_next(token) else NoneToken()


def has_next(token):
    return token.i + 1 <= len(token.doc) - 1


class NoneToken:
    def __getattribute__(self, name):
        return None
