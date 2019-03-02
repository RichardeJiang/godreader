from flask import render_template, json, jsonify, request
from flask_login import current_user, login_user
from app.models import User, Document
from app import app
from app import db

from gensim.summarization.summarizer import summarize

@app.route('/')
def index():
	print "MAS testing"
	return json.dumps({'ok': 1, 'test':2, 'ooo':3})
	# return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		print("logged in already")
		# return redirect(url_for('index'))
	response = {"loggedin": False}
	userInformation = json.loads(request.data)
	username = userInformation["username"]
	password = userInformation["password"]
	user = User.query.filter_by(username=username).first()
	print(user.password)
	print(username)
	print(password)
	if user is None or user.password != password:
		print("invalid user!")
		return json.dumps(response)
	else:
		response["loggedin"] = True
		return json.dumps(response)

	# form = LoginForm()
	# if form.validate_on_submit():
	# 	user = User.query.filter_by(username=form.username.data).first()
	# 	if user is None or not user.check_password(form.password.data):
	# 		flash('Invalid username or password')
	# 		return redirect(url_for('login'))
	# 	login_user(user, remember=form.remember_me.data)
	# 	return redirect(url_for('index'))
	# return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
	userInformation = json.loads(request.data)
	username = userInformation["username"]
	password = userInformation["password"]
	newUser = User(username=username, email=username, password = password)
	db.session.add(newUser)
	db.session.commit()
	return json.dumps({"registered": True})

@app.route('/getSummary')
def getSummary():
	textMessage = json.loads(request.data.decode('utf-8'))
	print(textMessage)
	summary = summarize(text = textMessage["content"])
	response = {'summary': summary, 'title': 'fixed'}
	return json.dumps(response)
	# return summarize(textMessage["content"])
