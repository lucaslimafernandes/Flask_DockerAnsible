from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask app!"

@app.route('/inter/')
def hehe():
    return 'nacional'

@app.route('/teste/')
def fn():
    return 'retorno teste'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5099)

