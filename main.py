from flask import Flask
from flask import render_template, request, redirect, session, url_for, escape, make_response, flash, abort

app = Flask(__name__)
app.secret_key = "bnNoqxXSgzoXSOezxpfdvadrMp5L0L4mJ4o8nRzn"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
	# close session
    return "logout"

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/report')
def report():
	return render_template('report.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True) 