import random

from flask import Flask, jsonify
from flask import request

from utils import json_abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/sentiment/')
def get_sentiment_of_text():
    text = request.args.get('text')
    if not text:
        return json_abort({
            'message': 'No input parameter text'
        }, 400)
    tokens = text.split(' ')
    result = []
    for token in tokens:
        if not token.isalpha():
            continue
        result.append({
            'token': token,
            'sentiment': random.random()
        })
    return jsonify(result)


if __name__ == '__main__':
    app.run()
