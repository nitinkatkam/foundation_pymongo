from pymongo import MongoClient
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

client = None  # TODO - Instantiate the MongoClient here, passing in the URI

@app.route('/')
def index():
  
  cursor_posts = None  # TODO - Call the .find() method on the collection
  list_posts = list(cursor_posts)

  return render_template('index.html', posts=list_posts)

@app.route('/post')
def post():
  return render_template('post.html')

@app.route('/post_save', methods=['POST'])
def post_save():
  subject = request.form['subject']
  body = request.form['body']
  # TODO - Call the .insert_one() method on the collection, passing in the document to insert
  return redirect('/')

