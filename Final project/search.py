from preprocess import preprocess
from tfidf import tfidf
from bm25 import bm25
from fasttext import fasttext
from elmo import elmo


def search(query, metric):
    query = preprocess(query)

    if metric=='tfidf':
        result = tfidf(query)
    elif metric=='bm25':
        result = bm25(query)
    elif metric=='fasttext':
        result = fasttext(query)
    elif metric=='elmo':
        result = elmo(query)

    return result