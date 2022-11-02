from flask import*
import sqlite3

app = Flask( __name__ )
app.secret_key="kuberan"

def init_db():
	db=sqlite3.connect('users.db')
	with open('schema.sql','r')as schema:
		db.executescript(schema.read())
	db.commit()
@app.cli.command('initdb')
def initdb_cmd():
    init_db()
    print("Initialised database.")

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def log_page():
	return render_template("home.html")

@app.route('/login')
def login():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		db = get_db()
		user = db.execute('SELECT password FROM users WHERE username = ?', (username, )).fetchone()

		if user is None:
			error = 'Incorrect Username/Password.'
		elif password != user['password']:
			print(user)
			error = 'Incorrect Password.'
		
		if error is None:
			return redirect(url_for('log_page'))
		flash(error)
		db.close()
	return render_template('login.html', error=error)

if __name__ == ' __main__ ':
	app.run(debug = True)