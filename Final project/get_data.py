import csv
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
            documents_2.append(row[2])
            data.append([int(row[0])])

    return data, documents_1, documents_2