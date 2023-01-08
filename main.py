"""
Test simple Flask application to learn CI with pylint
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """
    Main Function for home page of web app to display the test "Hello, World!!!"
    """
    return 'Hello, World!!!'
