import csv
import pymorphy2 as pm
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stopWords = set(stopwords.words('russian'))
morph = pm.MorphAnalyzer()


def get_data(file):
    '''Функция из файла делает списки запросов'''
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        documents_1 = []
        documents_2 = []
        data = []
        for row in reader:
            documents_1.append(row[1])

    return documents_1
documents_1 = get_data('quora_question_pairs_rus.csv')

def preprocess(text):
    """Функция на вход получает текст и возвращает список нормализованных слов, без знаков пунктуации, без стопслов"""
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    filtered_words = list(filter(lambda token: token not in stopwords.words('russian'), tokens))
    norm_words = [morph.parse(token)[0].normal_form for token in filtered_words]
    return norm_words

docs_processed = [preprocess(document) for document in documents_1]
with open('quora_question_pairs_rus.txt',  'w+', encoding='utf-8') as file:
    for doc in docs_processed:
        line = ' '.join(doc) + '\n'
        file.write(line)