from flask import Flask, render_template
from flask.views import MethodView
from pymodules.temperature import Temperature
from pymodules.calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return (render_template('index.html'))


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

if __name__ == '__main__':
    app.run()
