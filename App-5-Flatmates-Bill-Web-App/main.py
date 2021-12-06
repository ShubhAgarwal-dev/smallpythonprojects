from flask.views import MethodView
from werkzeug.wrappers import request
from wtforms import Form
from flask import Flask, render_template
from wtforms.fields.simple import StringField, SubmitField
from flatmate_bill.flat import Bill, Flatmate

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return (render_template('index.html'))


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return (render_template(
            'bill_form_page.html',
            billform=bill_form,
        ))


class ResultsPage(MethodView):

    def get(self):
        bill_form = BillForm(request.form)
        amount = bill_form.amount.data
        period = bill_form.period.data

        the_bill = Bill(int(amount), period)
        flatmate1 = Flatmate(bill_form.name1.data,
                             int(bill_form.days_in_house1.data))
        flatmate2 = Flatmate(bill_form.name2.data,
                             int(bill_form.days_in_house2.data))
        # currently it is made only for 2 people
        return f'{flatmate1._name} pays {flatmate1.pays(the_bill, flatmate2)}'


class BillForm(Form):
    amount = StringField('Bill Amount: ', default=1000)
    period = StringField('Bill Period(eg. Dec 2021): ', default='Dec 2021')

    name1 = StringField('Name of first flatmate: ', default='Ram')
    days_in_house1 = StringField('Number of days stayed in house: ', default=30)

    name2 = StringField('Name of first flatmate: ', default='Mohan')
    days_in_house2 = StringField('Number of days stayed in house: ', default=15)

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule(
    '/bill',
    view_func=BillFormPage.as_view('bill_form_page'),
    methods=['GET', 'POST'])
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
