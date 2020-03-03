import spacy
from nltk.stem import SnowballStemmer

from itm.publishing.domain.scholarship import AcademicLevel


nlp = spacy.load('es_core_news_md')
stemmer = SnowballStemmer('spanish')


def calculate_academic_level(item: dict):
    if 'description' not in item:
        return item

    item['academicLevel'] = match_academic_level(item['description']).value

    return item


def match_academic_level(raw_text):
    doc = first_sentence(raw_text)
    word = subtree_matcher(doc)[1]

    if word is None:
        return AcademicLevel.OTHERS

    for child in word.children:
        if child.dep_ == 'nmod':
            word = child
            break

    return academic_level(word.text)


def first_sentence(text):
    doc = nlp(text)
    return list(doc.sents)[0]


def subtree_matcher(doc):
    subject_ = None
    object_ = None

    for token in doc:
        if token.dep_ == 'nsubj':
            subject_ = token

        if token.dep_ == 'obj':
            object_ = token

        if subject_ and object_:
            break

    return (subject_, object_)


def academic_level(token):
    token = stemmer.stem(token)

    if is_undergraduate(token):
        return AcademicLevel.UNDERGRADUATE

    if is_postgraduate(token):
        return AcademicLevel.POSTGRADUATE

    return AcademicLevel.OTHERS


def is_undergraduate(token):
    words = ['estudiantes', 'bachilleres']
    words = map(stemmer.stem, words)
    return token in set(words)


def is_postgraduate(token):
    words = ['profesionales', 'doctorado', 'maestria', 'postdoctorado', 'posdoctorado']
    words = map(stemmer.stem, words)
    return token in set(words)
