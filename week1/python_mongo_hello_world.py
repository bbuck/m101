import pymongo, bottle

# this is the handler for the root address of the web server
@bottle.route("/")
def index():
  from pymongo import Connection
  connection = Connection('localhost', 27017)
  db = connection.test
  test = db.test
  item = test.find_one()
  return "<b>Hello %s</b>" % item["fname"]

bottle.run(host = "localhost", port = 8080)
