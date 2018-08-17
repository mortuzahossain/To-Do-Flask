from flask import Flask
app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
def hello():
    return "Index"

@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)