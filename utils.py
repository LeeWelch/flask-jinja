
movie_dict = [
  {"title": "Dune", "genre": "Sci-Fi", "rating":3},
  {"title": "Alien", "genre": "Sci-Fi", "rating":4},
  {"title": "Batman", "genre": "Comics", "rating":5}
]

def movie_stars(movie_dict):
  for movie in movie_dict:
    movie['stars'] = add_stars(movie['rating'])
  return movie_dict

  
def add_stars(rating):
  my_return = ""
  for x in range(5):
    checked ="checked" if rating > x else ""
    my_return += f"<span class=\"fa fa-star {checked}\"></span>"
  return my_return

  #<span class="fa-solid fa-star-half-stroke"></span>
  #put the above in an elif statement??