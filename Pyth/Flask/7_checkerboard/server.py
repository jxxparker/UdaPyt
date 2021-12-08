from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return render_template("index.html")

@app.route("/<rows>/<columns>")
def changeSquares(rows, columns):
    return render_template("change_squares.html", rows=int(rows), columns=int(columns))

if __name__ == "__main__":
    app.run(debug = True)