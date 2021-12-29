import pandas as pd
import sqlite3


class DatabaseDevelopment():
    """
    To construct the Dictionary database with ease
    """
    def __init__(self, database_path: str) -> None:
        self._dbpath = database_path
        self.make_databse(self._dbpath)
        return None

    @staticmethod
    def make_databse(database_path: str) -> None:
        connection = sqlite3.connect(database_path)
        connection.execute("""
            CREATE TABLE "Dictionary"(
                "word" TEXT,
                "meaning" TEXT
            );

            """)
        connection.commit()
        connection.close()
        return None

    def add_entry(self, word:str, meaning:str) -> None:
        """
        Adding entry to dictionary database.
        """
        connection = sqlite3.connect(self._dbpath)
        connection.execute("""
            INSERT INTO "Dictionary"("word", "meaning") VALUES (?, ?)
            """, [word, meaning])
        connection.commit()
        connection.close()
        return None


class CSVDataExtractor():

    def __init__(self, csv_filepath: str):
        self._csv_filepath = csv_filepath
        self._df = pd.read_csv(csv_filepath)

    def word_extractor(self, index:int):
        word_series = self._df["word"]
        return word_series[index]

    def meaning_extractor(self, index: int):
        meaning_series = self._df["definition"]
        return meaning_series[index]

if __name__ == '__main__':
    csv_data = CSVDataExtractor("data.csv")
    db = DatabaseDevelopment("data.db")

    for i, value in enumerate(csv_data._df["word"]):
        word = value
        meaning = csv_data._df["definition"][i]
        db.add_entry(word, meaning)
