from Flask import flask

app = Flask(__name__)

@app.route("/")
def index():
  return "TEST"

if __name__ == "__main__":
  app.run(port = 3000)
