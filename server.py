from flask import Flask, escape, request, render_template
import requests
import json
app = Flask(__name__)


@app.route('/')
def hello():
    filename = 'items.json'
    with open(filename) as f:
        item = json.load(f)
    return render_template('index.html', item=item)
