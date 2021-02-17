from flask import Flask,url_for,request

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello, Flask!!'

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello/<username>')
def greet(username):
    return 'Hello, %s!' % username

@app.route('/hello/<float:number>')
def multiply(number):
    return "{:.1f}".format(number*39)

@app.route('/get_welcome_url/<username>')
def show(username):
   return url_for('greet',username=username)

@app.route('/delete',methods=['POST'])
def seek():
    if request.method == 'POST':
        return 'POST SUCCEED' 

if __name__ == '__main__':
    app.debug = True
    app.run()
