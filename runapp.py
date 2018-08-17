import sqlite3 as sql
from flask import Flask,render_template

app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
@app.route("/index.html")
@app.route("/index.php")
def index():
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from todos")
	rows = cur.fetchall()
	return render_template('index.html',rows = rows)
	

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

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from todos")
   rows = cur.fetchall();
   print rows[0]["task"]
   return rows[0]["task"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)