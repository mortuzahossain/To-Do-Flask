from flask import Flask,render_template

app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
@app.route("/index.html")
@app.route("/index.php")
def index():
    return render_template('index.html')

@app.route("/update")
@app.route("/update.html")
def update():
    return render_template('update.html')

@app.route("/about")
def about():
    return "About"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)