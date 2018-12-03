from flask import Flask, jsonify
import requests
import json
import os

app = Flask(__name__)


@app.route("/")
def home():
    be_host = os.getenv('BACKEND_SERVICE_HOST', 'backend')
    be_port = os.getenv('BACKEND_SERVICE_PORT', '5000')
    url = 'http://{}:{}'.format(be_host, be_port)
    try:
        res = requests.get(url)
    except Exception:
        return "Error with {}".format(url)
    dictFromServer = res.json()
    return dictFromServer['message']


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
