from flask import Flask, render_template

#store functions here
import utils as utils

app = Flask(__name__)

movie_dict = [
  {"title": "Dune", "genre": "Sci-Fi", "rating":3},
  {"title": "Alien", "genre": "Sci-Fi", "rating":4},
  {"title": "Batman", "genre": "Comics", "rating":5}
]

movie_dict = utils.movie_stars(movie_dict)

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
