from flask import render_template, json, jsonify, request

from app import app

from gensim.summarization.summarizer import summarize

@app.route('/')
def index():
	print "MAS testing"
	return json.dumps({'ok': 1, 'test':2, 'ooo':3})
	# return render_template("index.html")


@app.route('/login')
def login():
	return

@app.route('/getSummary')
def getSummary():
	textMessage = json.loads(request.data.decode('utf-8'))
	print textMessage
	summary = summarize(text = textMessage["content"])
	response = {'summary': summary, 'title': 'fixed'}
	return json.dumps(response)
	# return summarize(textMessage["content"])
