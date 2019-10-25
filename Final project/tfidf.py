from sklearn.feature_extraction.text import TfidfVectorizer
from get_data import get_data
import numpy as np
from make_results import make_results

data, documents_1, documents_2 = get_data('quora_question_pairs_rus.csv')
vectorizer = TfidfVectorizer()
TFIDF_MATRIX = vectorizer.fit_transform(documents_1)


def tfidf(query, tfidf_matrix=TFIDF_MATRIX, vectorizer=vectorizer): #ДОБАВИТЬ ПРЕПРОЦЕСС В TFIDFVECTORIZER
    """
    Функция выполняет поиск по матрице tf-idf.
    """
    query_vector = np.zeros((TFIDF_MATRIX.shape[1], 1))
    for word in query:  # Для каждого слова нужно посчитать tfidf
        word_count = query.count(word) / len(query)

        try:
            word_index = vectorizer.get_feature_names().index(word)
            word_count_in_docs = TFIDF_MATRIX[word_index].nnz
            idf_word = np.log(TFIDF_MATRIX.shape[1] / word_count_in_docs)
            tfidf_word = word_count * idf_word
            query_vector[word_index] = tfidf_word
        except:
            tfidf_word = 0


    results = TFIDF_MATRIX @ query_vector
    sorted_indexes = np.argsort(results, axis=0)[::-1]
    sorted_tfidfs = np.sort(results, axis=0)[::-1]

    results_final = make_results(sorted_indexes, sorted_tfidfs, data=documents_1)
    return results_final