from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo
from passlib.hash import sha256_crypt

app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = 'your secret key'

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
        Recommendation1 = str(request.form['Recommendation1'])
        Recommendation2 = str(request.form['Recommendation2'])
        Recommendation3 = str(request.form['Recommendation3'])
        Recommendation4 = str(request.form['Recommendation4'])
        Recommendation5 = str(request.form['Recommendation5'])
        Recommendation6 = str(request.form['Recommendation6'])
        Recommendation7 = str(request.form['Recommendation7'])
        Recommendation8 = str(request.form['Recommendation8'])
        Recommendation9 = str(request.form['Recommendation9'])
        Recommendation10 = str(request.form['Recommendation10'])

        print(Name,Email,Batch,Role)

        return render_template('index.html', title="Result")

class RegisterForm(Form):
    name = StringField('Name', validators=[InputRequired(),Length(min=1, max=50)])
    username = StringField('Username', validators=[InputRequired(),Length(min=4, max=25)])
    email = StringField('Email', validators=[InputRequired(),Length(min=6 , max=50)])
    password = PasswordField('Password', validators=[InputRequired(),DataRequired(),EqualTo('confirm', message='Password do not match')])
    confirm = PasswordField('Confirm Password', validators=[InputRequired()])


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))

    return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Login Page")
        

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7700)