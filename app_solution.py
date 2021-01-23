from pymongo import MongoClient
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')

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

