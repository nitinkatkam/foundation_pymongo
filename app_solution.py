import json
from bson import ObjectId
from pymongo import MongoClient
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')

class JSONEncoder(json.JSONEncoder):
		def default(self, o):
				if isinstance(o, ObjectId):
						return str(o)
				return json.JSONEncoder.default(self, o)

@app.route('/')
def index():
	cursor_posts = client.pyprojectdb.posts.find()
	list_posts = list(cursor_posts)

	return render_template('index.html', posts=list_posts)
#  return '<!doctype html><html>Hello</html>'

@app.route('/post')
def post():
	return render_template('post.html')

@app.route('/post_save', methods=['POST'])
def post_save():
	#request.method
	subject = request.form['subject']
	body = request.form['body']
	client.pyprojectdb.posts.insert_one({'subject': subject, 'body': body})
	return redirect('/')

@app.route('/feed')
def feed():
	accumTxt = '['
	cursor_posts = client.pyprojectdb.posts.find()
	for iter in cursor_posts:
		if len(accumTxt) > 1:
			accumTxt += ', '
		accumTxt += JSONEncoder().encode(iter)
	accumTxt += ']'
	return accumTxt

