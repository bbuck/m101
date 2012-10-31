import bottle

@bottle.route("/")
def home_page():
  return "<html><head><title>Hello, World</title></head><body>Hello World</body></html>"

@bottle.route("/testpage")
def test_page():
  return "this is a test page"

bottle.debug(True)
bottle.run(host = "localhost", port = 8080)
