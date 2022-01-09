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
    price = seat_database.check_seat_price(seat_id)
    refund_price = price * 0.75
    bank.add_amount(card_number, cvc, refund_price)
    seat_database.update_seat_left(seat_id)
    return f'{refund_price} add to {card_number}'


def add_bank_user(card_type: str, card_number: int, cvc: int, holder: str,
                  balance: float):
    bank.add_user(card_type, card_number, cvc, holder, balance)
    return f"{card_number} added to tha baning database"


def seat_id_prompt():
    seat_id_char = input("Row name in which you want to have seat(A-J): ")
    seat_id_char = seat_id_char.upper()
    seat_id_number = int(input("Seat Number(1-10)?: "))
    seat_id = f"{seat_id_char}{seat_id_number}"
    return seat_id


def payment_prompt(seat_id):
    while True:
        card_number = int(input("Please enter your card number: "))
        cvc = int(input("Please enter the cvc"))
        if type((n := bank.read_balance(card_number, cvc))) != float:
            print("Please Check your cvc and card_number and try again.")
            continue
        else:
            price = seat_database.check_seat_price(seat_id)
            if n < price:
                print("Please another card.")
                print("Balance in this card is not enough!")
                continue
            else:
                price = seat_database.check_seat_price(seat_id)
                bank.deduct_amount(card_number, cvc, price)
                seat_database.update_seat_taken(seat_id)
                print(f"{seat_id} has now been booked.")
                break


if __name__ == "__main__":
    name = input("What is your full name? ")
    while True:
        seat_id = seat_id_prompt()
        if seat_database.check_seat_status(seat_id):
            print("Seat that you wanted to take is already full.")
            print("Please input another seat! ")
            continue
        else:
            payment_prompt(seat_id)
            break
    print("Thankyou for coming here for experience.")
