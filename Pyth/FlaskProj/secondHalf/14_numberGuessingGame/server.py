from flask import Flask, render_template, request, redirect, session, url_for
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes


app.run(host="localhost", port=8000, debug=True)