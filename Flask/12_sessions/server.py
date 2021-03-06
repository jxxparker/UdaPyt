from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Notice how the key we are using to access the info corresponds with the names
    # of the inputs from our html form
    name = request.form['name']
    email = request.form['email']
    return redirect('/') # redirects back to the '/' route

@app.route('/show')
def show_user():
    return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
    
if __name__=="__main__":
    app.run(debug=True)