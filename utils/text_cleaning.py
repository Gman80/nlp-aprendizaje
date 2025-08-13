import spacy
from nltk.corpus import stopwords

nlp = spacy.load("es_core_news_sm")
stop_es = set(stopwords.words("spanish"))

def limpiar_texto(texto):
    """ Preprocesa texto: elimina signos y stopwords, pasa a minúsculas y lematiza """
    doc = nlp(texto)
    tokens = [t.lemma_.lower() for t in doc if t.text.isalpha() and t.lemma_.lower() not in stop_es]
    return " ".join(tokens)