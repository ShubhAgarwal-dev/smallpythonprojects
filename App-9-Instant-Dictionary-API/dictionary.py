import csv


def dictionary(filepath):
    '''
    Just made it but it is not a very efficient
    way of doing it. Numpy arrays is a better
    option then this
    '''
    with open(fr'{filepath}', encoding='utf-8') as file:
        reader = csv.reader(file)
        heading = next(reader)
        dictionary_list = []
        for i, row in enumerate(reader):
            word_dict = {'word': row[0], 'definition': row[1]}
            dictionary_list.append(word_dict)
    return dictionary_list


if __name__ == '__main__':
    dictionary('data.csv')
