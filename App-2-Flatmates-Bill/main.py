from fpdf import FPDF


class Bill():
    '''
    Object that contain data about bill.
    Such as total amount, period of bill, etc.
    '''

    def __init__(self, amount: int, period: int) -> None:
        self._amount = amount
        self._period = period


class Flatmate():
    '''
    Object for flatmate(or anyone for that matter) that live with you 
    and pays share of bill.
    '''

    def __init__(self, name: str, days_in_house: int = 30) -> None:
        self._name = name
        self._days = days_in_house

    def pays(self, bill: Bill, *flatmates):
        sum = self._days
        for i in flatmates:
            sum += i._days
        weight = self._days / sum
        return weight * bill._amount


class PdfReport():
    '''
    It would create pdf file that would contain data about flatmate's name, due bill, etc.
    '''

    # # sire od A4 in points is 595 x 842 pt

    def __init__(self, file_name: str):
        self._file_name = file_name

    def generate_pdf(self, bill: Bill, *flatmates: Flatmate):
        '''
        it is everything what this class is about
        '''
        # making pdf class
        pdf = FPDF(orientation='L', unit='pt', format='A4')
        pdf.add_page()

        # Inserting Title
        pdf.set_font(family="Arial", style='BI', size=32)
        pdf.cell(w=0, h=100, txt="Bill", border=1, ln=1, align='C')
        # W=0 would extend the margin upto the right margin

        # Inserting values
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=390, h=50, txt='Period', border=1, ln=0, align='c')
        pdf.cell(w=0, h=50, txt=bill._period, border=1, ln=1, align='C')
        pdf.cell(w=0, h=10, ln=1)

        # Adding Name and due amount of flatmate
        pdf.set_font(family='Times', size=20)
        for flatmate in flatmates:

            flatmates_list = list(flatmates)
            flatmates_list.remove(flatmate)
            flatmates2 = tuple(flatmates_list)

            amount_to_pay = flatmate.pays(bill, *flatmates2)

            pdf.cell(w=390, h=50, txt=flatmate._name, border=1, ln=0)
            pdf.cell(
                w=0,
                h=50,
                txt=str(format(amount_to_pay, ".2f")),
                border=1,
                ln=1,
                align='R')

        pdf.cell(w=390, h=50, txt="Total Amount", border=1, ln=0)
        pdf.cell(
            w=0,
            h=50,
            txt=str(format(float(bill._amount), ".2f")),
            border=1,
            ln=1,
            align='R')

        # Output Cell
        pdf.output(fr".\pdf\{self._file_name}")


if __name__ == '__main__':
    shivam = Flatmate('Shivam')
    rahul = Flatmate('Rahul', 20)
    meena = Flatmate('Meena', 18)
    electricity_bill = Bill(1200, 'Dec 2021')

    print(shivam.pays(electricity_bill, rahul, meena))
    print(rahul.pays(electricity_bill, shivam, meena))
    print(meena.pays(electricity_bill, shivam, rahul))

    PDF = PdfReport("bill.pdf")
    PDF.generate_pdf(electricity_bill, shivam, rahul, meena)
