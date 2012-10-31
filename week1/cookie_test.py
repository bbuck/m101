import bottle

@bottle.route("/")
def home_page():
  fruits = [ "apple", "banana", "orange", "peach" ]
  return bottle.template("template_test", { "name": "Brandon", "fruits": fruits })

@bottle.post("/favorite_fruit")
def favorite_fruit():
  fruit = bottle.request.forms.get("fruit")
  if fruit == None or fruit == "":
    fruit = "No Fruit Selected"
  bottle.response.set_cookie("fruit", fruit)
  bottle.redirect("/show_fruit")

@bottle.route("/show_fruit")
def show_fruit():
  fruit = bottle.request.get_cookie("fruit")
  return bottle.template("favorite_fruit", { "fruit": fruit })

bottle.debug(True)
bottle.run(host = "localhost", port = 8080)
