from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from registerform import RegisterForm

app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = 'your secret key'

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password123#@!'
app.config['MYSQL_DB'] = 'kt'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('login'))

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        Name = request.form['Name']
        Email = request.form['Email']
        Batch = request.form['Batch']
        Role = request.form['Role']
        Question1 = int(request.form['Question1'])
        Question2 = int(request.form['Question2'])
        Question3 = int(request.form['Question3'])
        Question4 = int(request.form['Question4'])
        Question5 = int(request.form['Question5'])
        Question6 = int(request.form['Question6'])
        Question7 = int(request.form['Question7'])
        Question8 = int(request.form['Question8'])
        Question9 = int(request.form['Question9'])
        Question10 = int(request.form['Question10'])
        Remark1 = str(request.form['Remark1'])
        Remark2 = str(request.form['Remark2'])
        Remark3 = str(request.form['Remark3'])
        Remark4 = str(request.form['Remark4'])
        Remark5 = str(request.form['Remark5'])
        Remark6 = str(request.form['Remark6'])
        Remark7 = str(request.form['Remark7'])
        Remark8 = str(request.form['Remark8'])
        Remark9 = str(request.form['Remark9'])
        Remark10 = str(request.form['Remark10'])

        total_score = Question1+Question2+Question3+Question4+Question5+Question6+Question7+Question8+Question9+Question10
        avg_score = total_score/10
        percent_scored = avg_score/5 * 100

        return render_template('result.html', title="Result", name=Name, score = "{:0.2f} %".format(percent_scored))

    return render_template('index.html', title="Feedback Portal")
    

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.hash(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
        
# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():

    return render_template('mainpage.html', title="Dashboard")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7700)
