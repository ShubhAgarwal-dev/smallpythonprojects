from cinema.db import *

bank = Banking()
seat_database = Cinema()


def sell_seat(seat_id: str, card_number: int, cvc: int):
    check_balance = bank.read_balance(card_number, cvc)
    if type(check_balance) == float:
        if not seat_database.check_seat_status(seat_id):
            price = seat_database.check_seat_price(seat_id)
            if price > check_balance:
                bank.deduct_amount(card_number, cvc, price)
                seat_database.update_seat_taken(seat_id)
                return f"{seat_id} is now booked"
            else:
                return "Check your balance and try again."
    else:
        return check_balance


def refund_process(seat_id, card_number, cvc):
    pass


def add_bank_user(card_type: str, card_number: int, cvc: int, holder: str,
                  balance: float):
    bank.add_user(card_type, card_number, cvc, holder, balance)
    return f"{card_number} added to tha baning database"


if __name__ == "__main__":
    pass
