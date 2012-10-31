import bottle

@bottle.route("/")
def index_page():
  data = { "name": "Brandon", "fruits": [ "apple", "banana", "tomato" ] }
  return bottle.template("template_test", data)

bottle.run(host = "localhost", port = 8080)
