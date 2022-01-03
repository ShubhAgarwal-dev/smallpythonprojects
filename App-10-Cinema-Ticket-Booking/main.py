from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/booking')
def booking_page():
    return "Work in Progress"


if __name__ == '__main__':
    app.run(debug=True)
