from flat import *
from generatepdf import *
# I know that this could result in name conflict when working with bigger modules\
# but currently it would not be causing issues

if __name__ == '__main__':
    time = str(input('What is the time period of bill ? eg. Dec 2020: '))
    amount = int(input('Enter Amount of the bill: '))
    bill = Bill(amount, time)

    while True:
        try:
            n = int(input('How many people have to share the given bill?: '))
            if n <= 0:
                print('How can number of people be less than or equal to 0?')
                print("Please try again!")
        except ValueError as err:
            print(f'Please enter a number\n{err}\nTry Again!')
            continue
        except TypeError as err:
            print(f'Please enter anything that makes sense\n{err}\nTry Again!')
            continue
        else:
            flatmates = []
            for i in range(n):
                name = str(
                    input(f'What is the name of flatmate/roommate {i+1}: '))
                days = int(
                    input(f'No. of days {name} Lived inside the flat/room: '))
                flatmates.append(Flatmate(name, days))
            break

    filename = str(
        input(
            "What is the name of the share pdf generated? eg. electricity bill : "
        )) + '.pdf'
    pdf = PdfReport(filename)
    pdf.generate_pdf(bill, *flatmates)
    print('If not opened check pdf folder for bill')