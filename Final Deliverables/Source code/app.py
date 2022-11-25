from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

app = Flask(__name__)
app.debug = True

app.secret_key='75v7578567c674r67v7tbi88i'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=your_host_name;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=your_user_name;PWD=your_password",'','')

@app.route('/', methods=['GET', 'POST'])
def login():
    global userid
    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM users WHERE username =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid = account['USERNAME']
            session['username'] = account['USERNAME']
            msg = 'Logged in successfully !'

            msg = 'Logged in successfully !'
            return render_template('main.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    else:
        return render_template('login.html', msg=msg)



@app.route('/main')  
def main():  
      return render_template('main.html')

@app.route('/signup', methods = ('POST','GET'))  
def signup():  
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM users WHERE username =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            insert_sql = "INSERT INTO  users VALUES (?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, username)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)
	  
@app.route('/shoes', methods = ('POST','GET'))
def shoes():
	msg = ''
	if request.method == 'POST':
		product = 'shoes'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('shoes.html',msg=msg)
	return render_template('shoes.html',msg=msg)

@app.route('/saree', methods = ('POST','GET'))
def saree():
	msg = ''
	if request.method == 'POST':
		product = 'saree'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('saree.html',msg=msg)
	return render_template('saree.html',msg=msg)

@app.route('/bag', methods = ('POST','GET'))
def bag():
	msg = ''
	if request.method == 'POST':
		product = 'bag'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('bag.html',msg=msg)
	return render_template('bag.html',msg=msg)
	
@app.route('/book')
def book():
	msg = ''
	if request.method == 'POST':
		product = 'book'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('book.html',msg=msg)
	return render_template('book.html',msg=msg)	

@app.route('/laptop', methods = ('POST','GET'))
def laptop():
	msg = ''
	if request.method == 'POST':
		product = 'laptop'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('laptop.html',msg=msg)
	return render_template('laptop.html',msg=msg)		

@app.route('/tv', methods = ('POST','GET'))
def tv():
	msg = ''
	if request.method == 'POST':
		product = 'Television'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('tv.html',msg=msg)
	return render_template('tv.html',msg=msg)

@app.route('/phone', methods = ('POST','GET'))
def phone():
	msg = ''
	if request.method == 'POST':
		product = 'phone'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('phone.html',msg=msg)
	return render_template('phone.html',msg=msg)

@app.route('/watch', methods = ('POST','GET'))
def watch():
	msg = ''
	if request.method == 'POST':
		product = 'watch'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('watch.html',msg=msg)
	return render_template('watch.html',msg=msg)

@app.route('/shirt', methods = ('POST','GET'))
def shirt():
	msg = ''
	if request.method == 'POST':
		product = 'shirt'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('shirt.html',msg=msg)
	return render_template('shirt.html',msg=msg)

@app.route('/jeans', methods = ('POST','GET'))
def jeans():
	msg = ''
	if request.method == 'POST':
		product = 'jeanspant'
		name = request.form['name']
		mail = request.form['mail']
		address = request.form['address']
		mobile = request.form['mobile']
		quantity = request.form['quantity']
		sql = "SELECT * FROM orders;"
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		print(account)
		insert_sql = "INSERT INTO  orders VALUES (?, ?, ?, ?, ?, ?)"
		prep_stmt = ibm_db.prepare(conn, insert_sql)
		ibm_db.bind_param(prep_stmt, 1, name)
		ibm_db.bind_param(prep_stmt, 2, product)
		ibm_db.bind_param(prep_stmt, 3, mail)
		ibm_db.bind_param(prep_stmt, 4, address)
		ibm_db.bind_param(prep_stmt, 5, quantity)
		ibm_db.bind_param(prep_stmt, 6, mobile)
		ibm_db.execute(prep_stmt)
		msg = 'You have successfully ordered !'
		return render_template('jeans.html',msg=msg)
	return render_template('jeans.html',msg=msg)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global userid
    msg = ''

    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM admin WHERE name =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, name)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['NAME']
            userid = account['NAME']
            session['name'] = account['NAME']
            msg = 'Logged in successfully !'

            msg = 'Logged in successfully !'
            return render_template('adminportal.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    else:
        return render_template('admin.html', msg=msg)

@app.route('/users')
def users():
	global userid
	accounts = []
	sql = "SELECT * FROM users"
	stmt = ibm_db.prepare(conn, sql)
	ibm_db.execute(stmt)
	account = ibm_db.fetch_assoc(stmt)
	print(account)
	while account:
		accounts.append(account)
		account = ibm_db.fetch_assoc(stmt)
	return render_template('users.html',data=accounts)

@app.route('/orders')
def orders():
	global userid
	accounts = []
	sql = "SELECT * FROM orders"
	stmt = ibm_db.prepare(conn, sql)
	ibm_db.execute(stmt)
	order = ibm_db.fetch_assoc(stmt)
	while order:
		accounts.append(order)
		order = ibm_db.fetch_assoc(stmt)
	return render_template('orders.html',data=accounts)
