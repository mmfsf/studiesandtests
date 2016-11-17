from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/point', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(str(request.form['latitude']))
        print(str(request.form['longitude']))
        return "0"