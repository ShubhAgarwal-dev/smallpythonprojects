from flask import Flask, render_template
from flask.views import MethodView
from flask import request

from wtforms.fields.simple import StringField, SubmitField
from wtforms import Form

from pymodules.temperature import Temperature
from pymodules.calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):
    '''
    Just a home page made for sake of it
    '''

    def get(self):
        return (render_template('index.html'))


class CalorieFormPage(MethodView):
    '''
    To calculate the calories
    '''

    def get(self):
        calories_form = CalorieForm()
        return render_template(
            'calories_form_page.html', caloriesform=calories_form)

    def post(self):
        calories_form = CalorieForm(request.form)
        temp = Temperature(calories_form.city.data, calories_form.country.data)
        weight = float(calories_form.weight.data)
        height = float(calories_form.age.data)
        age = int(calories_form.age.data)
        calories = Calorie(weight, height, age, temp.get())

        return render_template(
            'calories_form_page.html',
            caloriesform=calories_form,
            result=True,
            calories=calories.calculate())


class CalorieForm(Form):
    '''
    The form making class
    '''
    weight = StringField('Weight(in Kg): ', default=70)
    height = StringField('Height(in cm): ', default=173)
    age = StringField('Age(in years): ', default=32)
    city = StringField('City Name: ', default='Shahjahanpur')
    country = StringField('Country: ', default='India')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule(
    '/calories_form',
    view_func=CalorieFormPage.as_view('calories_form_page'),
    methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()
