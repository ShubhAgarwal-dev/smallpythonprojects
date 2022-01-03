import sqlite3
from typing import final


class Banking():

    def __init__(self, database_path: str = 'banking.db') -> None:
        self._database_path = database_path

    def add_user(self, card_type: str, card_number: int, cvc: int, holder: str,
                 balance: float):
        """
        To add a new user to the banking database.
        """
        connection = sqlite3.connect(self._database_path)
        connection.execute(
            """
            INSERT INTO "Card"("type","number","cvc","holder","balance") VALUES(?,?,?,?,?)
            """,
            [card_type,
             int(card_number),
             int(cvc), holder,
             float(balance)])
        connection.commit()
        connection.close()
        return None

    def read_balance(self, card_number: int, cvc: int):
        connection = sqlite3.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT "balance" FROM "Card" WHERE "number" = ? and "cvc" = ?
            """, [int(card_number), int(cvc)])
        result = cursor.fetchall()
        connection.close()
        for i, value in enumerate(result):
            balance = result[i][0]
        return balance

    def deduct_amount(self, card_number: int, cvc: int, amount: float):
        initial_amount = self.read_balance(card_number, cvc)
        final_amount = initial_amount - amount
        if final_amount < 0:
            raise ValueError("Total amount is low, transaction aborted")
        connection = sqlite3.connect(self._database_path)
        connection.execute(
            """
            UPDATE "Card" SET "balance" = ? WHERE "number" = ? AND "cvc" = ?
            """, [final_amount, card_number, cvc])
        connection.commit()
        connection.close()
        return None

    def add_amount(self, card_number: int, cvc: int, amount: float):
        initial_amount = self.read_balance(card_number, cvc)
        final_amount = initial_amount + amount
        connection = sqlite3.connect(self._database_path)
        connection.execute(
            """
            UPDATE "Card" SET "balance" = ? WHERE "number" = ? AND "cvc" = ?
            """, [final_amount, card_number, cvc])
        connection.commit()
        connection.close()
        return None

    @staticmethod
    def _make_database(db_path: str):
        connection = sqlite3.connect(db_path)
        connection.execute("""
            CREATE TABLE "Card"(
                "type" TEXT,
                "number" INTEGER,
                "cvc" INTEGER,
                "holder" TEXT,
                "balance" REAL
            );

        """)
        connection.commit()
        connection.close()
