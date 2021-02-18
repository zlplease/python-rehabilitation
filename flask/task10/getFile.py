from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route('/get_file_url/<filename>')
def hello_world(filename):
    fileUrl = url_for('static', filename = filename)
    return 'http://127.0.0.1:5000{}'.format(fileUrl)

@app.route('/get_file/<filename>')
def direct(filename):
    return redirect(url_for('static', filename = filename))

if __name__ == '__main__':
    app.debug = True
    app.run()