from csvtodb import *


def defination(word: str):
    '''
    Just made it but it is not a very efficient
    way of doing it. Numpy arrays is a better
    option then this
    '''
    return tuple(DatabaseDevelopment.get_defination('data.db', word))

if __name__ == '__main__':
    print(defination('acid'))
