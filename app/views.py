from flask import render_template, json, jsonify, request
from flask_login import current_user, login_user
from app.models import User, Document
from app import app
from app import db
import string

from gensim.summarization.summarizer import summarize

@app.route('/')
def index():
	# print "MAS testing"
	return json.dumps({'ok': 1, 'test':2, 'ooo':3})
	# return render_template("index.html")

@app.route('/adddata')
def add():
	user1 = User(username="yanzhe", password="testpass")
	user2 = User(username="shenhao", password="testpass")
	user3 = User(username="xiaoming", password="testpass")
	db.session.add(user1)
	db.session.add(user2)
	db.session.add(user3)
	doc = Document(holder=user1, title="testingtitle", original_text="testtext", summary="testsummary")
	db.session.add(doc)

	db.session.commit()

	return json.dumps({'result': 'successful'})


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_active:
		print("logged in already")
	else:
		print("logging in?")
		# return redirect(url_for('index'))
	response = {"loggedin": False, "Error": "None", "User": "None"}
	userInformation = json.loads(request.data)
	username = userInformation["username"]
	password = userInformation["password"]
	user = User.query.filter_by(username=username).first()
	print(user.password)
	print(username)
	print(password)
	if user is None or user.password != password:
		print("invalid user!")
		response["Error"] = "Invalid username or password!"
		# return json.dumps(response)
	else:
		login_user(user)
		response["loggedin"] = True
		response["User"] = username
		myDocs = user.documents
		titleList = [d.title for d in myDocs]
		response["mydocs"] = titleList
	
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
	response = {"registered": False, "error": "None"}
	userInformation = json.loads(request.data)
	username = userInformation["username"]
	password = userInformation["password"]
	if User.query.filter_by(username=username).first() is not None:
		response["error"] = "User already exists!"
		return json.dumps(response)
	newUser = User(username=username, email=username, password = password)
	db.session.add(newUser)
	db.session.commit()
	response["registered"] = True
	return json.dumps(response)

@app.route('/getSummary', methods=['GET', 'POST'])
def getSummary():
	print(request)
	textMessage = json.loads(request.data)
	# print(textMessage)
	summary = summarize(text = textMessage["content"])
	response = {'summary': summary, 'title': 'fixed'}
	return json.dumps(response)
	# return summarize(textMessage["content"])
