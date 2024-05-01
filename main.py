from flask import Flask, render_template, request, url_for

#create a secret key for security
import os

#store functions here
import utils as utils

import json

app = Flask(__name__)

#secret key for form security 
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

@app.route('/user/<int:user_number>')
def user(user_number):
    return f'Content for User {user_number}'


#user list
@app.route('/users')
def users():

  # Read project data from JSON file
  with open('test.json') as json_file:
      user_data = json.load(json_file)
      #print(user_data)

  context = {
    "title": "Users",
    "users": user_data
  }

  return render_template("users.html",**context)

# Route for the form page
@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Register"
    feedback = None
    if request.method == 'POST':
        feedback = utils.register_data(request.form)

    context = {
        "title": title,
        "feedback": feedback
    }
    return render_template('register.html', **context)

@app.route('/')
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    title = "About"
    return render_template("about.html", title=title)



@app.route('/movies')
def movies():
  
  movie_dict = utils.movie_stars(utils.movie_dict)
  
  context = {
      "title" : "Movies",
      "movies" : movie_dict
    }
  return render_template("movies.html", **context)

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)

@app.route('/gallery')
def gallery():
    title = "Gallery"
    return render_template("gallery.html", title=title)


app.run(host='0.0.0.0', port=81)
