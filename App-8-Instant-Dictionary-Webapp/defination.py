# This could also be improved furtuer by using the dictionary api available online

import pandas as pd


class Defination():

    def __init__(self, term) -> None:
        self._term = term

    def get(self):
        data_frame = pd.read_csv('data.csv')
        term_data_frame = data_frame.loc[data_frame['word'] == self._term]
        term_defination = term_data_frame['definition']
        return tuple(term_defination)


if __name__ == '__main__':
    alfabetagamma = Defination('acid')
    print(alfabetagamma.get())
