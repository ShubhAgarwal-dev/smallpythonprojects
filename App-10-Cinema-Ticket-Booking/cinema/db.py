import sqlite3
from os.path import isfile
from string import ascii_uppercase


class Banking():
    """
    Just a databasse class, performs all the transactions
    required for booking the ticket
    """

    def __init__(self, database_path: str = 'banking.db') -> None:
        """
        Create the database if it does not exist by default.
        """
        self._database_path = database_path
        if not isfile(path=database_path):
            self._make_database(self._database_path)
            # now it would automatically make the database if not already formed

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
        while True:
            try:
                return balance
            except UnboundLocalError:
                return "Check your card number and cvc anf try again."

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
        return None


class Cinema():

    def __init__(self, database_path: str = 'cinema.db') -> None:
        self._database_path = database_path
        if not isfile(database_path):
            self._make_database(self._database_path)
            price = 100
            for i, letter in enumerate(ascii_uppercase):
                for m in range(1, 11):
                    seat_id = letter + str(m)
                    self.add_seats(seat_id, 0, price)
                if i > 8:
                    break
                price += 10

    @staticmethod
    def _make_database(db_path: str) -> None:
        connection = sqlite3.connect(db_path)
        connection.execute("""
            CREATE TABLE "Seat" (
                "seat_id"	TEXT,
                "taken"	INTEGER,
                "price"	REAL
            );

        """)
        connection.commit()
        connection.close()
        return None

    def add_seats(self, seat_id: str, taken: bool, price: float) -> None:
        connection = sqlite3.connect(self._database_path)
        connection.execute(
            """
            INSERT INTO "Seat"("seat_id", "taken", "price") VALUES(?,?,?)
        """, [seat_id, int(taken), float(price)])
        connection.commit()
        connection.close()
        return None


if __name__ == "__main__":
    theare_seat_db = Cinema()