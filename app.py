from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7700)