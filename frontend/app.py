from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    url = "http://backend:5000/"
    try:
        res = requests.get(url)
    except ConnectionError:
        return "Error with {}".format(url)
    dictFromServer = res.json()
    return dictFromServer['message']


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
