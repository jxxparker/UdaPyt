from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', first_name="ghoney", last_name="Park")

@app.route('/dojo')
def dojo():
    return "dojo"

if __name__ == "__main__":
    app.run(debug=True)  


