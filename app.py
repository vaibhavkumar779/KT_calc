from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
#from flask_mysqldb import MySQL
from registerform import RegisterForm
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

        return render_template('result.html', title="Result", name=Name, score = "{} %".format(percent_scored))

    return render_template('index.html', title="Feedback Portal")
    
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