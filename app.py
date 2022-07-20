from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title="Home Page")

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', title="Login Page")


@app.route('/score', methods=['GET','POST'])
def score():
    if request.method == 'POST':
        Name = request.form['Name']
        Email = request.form['Email']
        Batch = request.form['Batch']
        Role = request.form['Role']
        

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7700)