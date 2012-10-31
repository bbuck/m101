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
  return bottle.template("favorite_fruit", { "fruit": fruit })

bottle.debug(True)
bottle.run(host = "localhost", port = 8080)
