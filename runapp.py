import sqlite3 as sql
from flask import Flask,render_template,request

app = Flask(__name__)

def todolists():
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from todos")
	return cur.fetchall()

@app.route("/",methods = ['POST', 'GET'])
@app.route("/index",methods = ['POST', 'GET'])
@app.route("/index.html",methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		try:
			task = request.form['todo']
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO todos (task) VALUES (?)",(task,))
				con.commit()
		except Exception as e:
			raise e
		return render_template('index.html',rows = todolists())
	else:
		return render_template('index.html',rows = todolists())

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