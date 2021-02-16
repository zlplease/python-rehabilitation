from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!!'

@app.route('/index')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.debug = True
    app.run()