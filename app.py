from flask import Flask
from db import countries

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello"
