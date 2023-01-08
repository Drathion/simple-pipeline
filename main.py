"""
Test simple Flask application to learn CI with pylint
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    """
    hello Function for home page of web app to display the test "Hello, World!!!"
    """
    return 'Hello, World!!!'


def main():
    """
    Function that runs web server
    """
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
