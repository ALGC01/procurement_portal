from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-form')
def request_form():
    return render_template('request_form.html')


@app.route('/requests')
def list_requests():
    return render_template('list_requests.html')


@app.route('/submit', methods=['POST'])
def submit_request():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)