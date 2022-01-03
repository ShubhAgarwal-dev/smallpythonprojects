import sqlite3


class Banking():

    def __init__(self, database_path) -> None:
        self._database_path = database_path
        pass