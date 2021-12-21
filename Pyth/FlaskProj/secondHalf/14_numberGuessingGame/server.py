from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "MySecretKey?!"




if __name__=="__main__":
    app.run(host="localhost", port=8000, debug=True)
