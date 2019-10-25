from get_data import get_data
import numpy as np
from preprocess import preprocess
from gensim.models import FastText
data, documents_1, documents_2 = get_data('quora_question_pairs_rus.csv')
index2doc = dict(enumerate(documents_1))
docs_processed = [preprocess(document) for document in documents_1[:10000]]

f_model = FastText(size=4, window=3, min_count=1)  # instantiate
f_model.build_vocab(sentences=docs_processed)
f_model.train(sentences=docs_processed, total_examples=len(docs_processed), epochs=100)

def cos_sim(v1, v2):
    return np.inner(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def fasttext_matrix(data=docs_processed):
    ft_matrix = []
    for document in data:
        empty_m = np.zeros((len(document), f_model.vector_size))
        for i, element in enumerate(document):
            if element in f_model.wv:
                empty_m[i] = f_model.wv[element]
        if empty_m.shape[0] != 0:
            vector = np.mean(empty_m, axis=0)
        ft_matrix.append(vector)
    ft_matrix = np.array(ft_matrix)
    print('ft bilt')
    return ft_matrix
ft_matrix=fasttext_matrix()

def fasttext(query, ft_matrix=ft_matrix):
  query = [query]
  query_vec = fasttext_matrix(query)[0]
  result = {}

  for i, document_vec in enumerate(ft_matrix):
    sim = cos_sim(query_vec, document_vec)
    result[sim] = index2doc[i]
  final_result = sorted(result.items(), key=lambda x: x[0], reverse=True)[:10]

  final=[]
  for el in final_result:
      element = str(el[0]) + " - " + str(el[1])
      final.append(element)
  return final
