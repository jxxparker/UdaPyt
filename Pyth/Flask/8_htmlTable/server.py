from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def initial():
    return render_template("index.html")


@app.route('/index')
def index1():
    users = (
        {'first_name': 'Ghoney', 'last_name': 'Park'},
        {'first_name': 'John', 'last_name': 'kim'},
        {'first_name': 'Mark', 'last_name': 'Choi'},
        {'first_name': 'Kobe', 'last_name': 'Bryant'},
        {'first_name': 'Michael', 'last_name': 'Jordan'},
    )
    return render_template("index1.html", user=users)


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
