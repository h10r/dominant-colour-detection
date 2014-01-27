#!/opt/local/bin/python3.3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about/')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run()