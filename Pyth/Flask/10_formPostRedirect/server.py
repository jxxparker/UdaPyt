from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['POST'])
def create():
    print(request.form)
    print('Name', request.form['name'])
    print('Number', request.form['number'])
    
    name = request.form['name']
    number = request.form['number']
    return render_template("create.html")

if __name__=="__main__":
    app.run(host="localhost", port=8000, debug=True)
