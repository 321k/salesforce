from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/callback', methods=['POST'])
def salesforce():
    print(request)
    return 'Hello, World!'