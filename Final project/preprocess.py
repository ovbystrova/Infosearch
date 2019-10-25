import re
import pymorphy2 as pm
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stopWords = set(stopwords.words('russian'))
morph = pm.MorphAnalyzer()

def preprocess(text):
    """Функция на вход получает текст и возвращает список нормализованных слов, без знаков пунктуации, без стопслов"""
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    filtered_words = list(filter(lambda token: token not in stopwords.words('russian'), tokens))
    norm_words = [morph.parse(token)[0].normal_form for token in filtered_words]
    return norm_words