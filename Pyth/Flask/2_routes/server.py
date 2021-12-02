from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/')
def hello_word():
    return "Hello World!"

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__=="__main__":

    app.run(debug=True)

