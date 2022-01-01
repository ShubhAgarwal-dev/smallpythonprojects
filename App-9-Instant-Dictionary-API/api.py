import flask
from flask import render_template
from flask import request, jsonify

from dictionary import defination

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'go to /api/v1/meaning and provide word as param and the word you want to find meaning of as param'


@app.route('/api/v1/meaning', methods=['GET'])
# to handel request for /api/v1/meaning?word=
def meaning_word():
    # Checking if word is provided in the url
    if 'word' in request.args:
        word = str(request.args['word'])
    else:
        # It could have been a simple error message
        #but I went with something unique
        return render_template('404notfound.html')

    responce = {'word': word, 'definition': defination(word)}
    return jsonify(responce)


if __name__ == '__main__':
    app.run()
