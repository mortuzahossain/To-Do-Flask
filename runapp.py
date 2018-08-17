import sqlite3 as sql
from flask import Flask,render_template,request

app = Flask(__name__)

def todolists():
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from todos")
	return cur.fetchall()

def singletodo(id):
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM todos WHERE id = ?",(id,))
	return cur.fetchall()[0]

def deteletodo(id):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("DELETE FROM todos WHERE id = ?",(id,))
	con.commit()
	return

def updatetodo(id,task):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("UPDATE todos SET task = ? WHERE id = ?",(task,id,))
	con.commit()
	return



# FOR INDEX PAGE
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

# FOR UPDATE PAGE
@app.route("/update/<id>",methods = ['POST', 'GET'])
def update(id):
	if request.method == 'POST':
		task = request.form['todo']
		updatetodo(id,task)
	data = singletodo(id)
	return render_template('update.html',data = data)

# FOR DELETE
@app.route("/delete/<id>")
def delete(id):
	deteletodo(id)
	return render_template('index.html',rows = todolists())

# FOR ABOUT PAGE -- UNDER CONSTRUCTION
@app.route("/about")
def about():
    return "About"

# FOR 404 ERROR
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)