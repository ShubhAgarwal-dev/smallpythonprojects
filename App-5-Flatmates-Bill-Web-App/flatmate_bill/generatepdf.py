from fpdf import FPDF
import webbrowser
from flat import *

# Code from main.py is being reorganized


class PdfReport():
    '''
    It would create pdf file that would contain data about flatmate's name, due bill, etc.
    '''

    # # size of A4 in points is 595 x 842 pt

    def __init__(self, file_name: str):
        self._file_name = file_name

    def generate_pdf(self, bill: Bill, *flatmates: Flatmate):
        '''
        it is everything what this class is about
        '''
        # making pdf class
        pdf = FPDF(orientation='L', unit='pt', format='A4')
        pdf.add_page()
        #   # I did not add image available at files\house.png as it was not looking good

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
        total = bill._amount
        # Because it is to be printed at last line
        for flatmate in flatmates:

            flatmates_list = list(flatmates)
            flatmates_list.remove(flatmate)
            flatmates = tuple(flatmates_list)

            amount_to_pay = flatmate.pays(bill, *flatmates)

            pdf.cell(w=390, h=50, txt=flatmate._name, border=1, ln=0)
            pdf.cell(
                w=0,
                h=50,
                txt=str(format(amount_to_pay, ".2f")),
                border=1,
                ln=1,
                align='R')
            bill._amount -= amount_to_pay

        pdf.cell(w=390, h=50, txt="Total Amount", border=1, ln=0)
        pdf.cell(
            w=0,
            h=50,
            txt=str(format(float(total), ".2f")),
            border=1,
            ln=1,
            align='R')

        # Output Cell
        pdf.output(fr".\pdf\{self._file_name}")
        webbrowser.open(fr'.\pdf\{self._file_name}')
