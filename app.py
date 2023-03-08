from flask import Flask
from db import countries

app = Flask(__name__)


# git manages our code
# github helps to host our online

@app.route('/')
def home():
    return countries
