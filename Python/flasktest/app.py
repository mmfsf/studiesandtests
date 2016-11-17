import json
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    quote = {
            'message': 'Hello, World!'
        }
    return json.dumps(quote)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8888)