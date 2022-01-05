from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "MySecretKey?!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        session['counter'] = 0
        return render_template('index.html')
    elif request.method == 'POST':
        inc_value = request.form['button']
        if inc_value == '+1':
            session['counter'] += 1
        elif inc_value == '+2':
            session['counter'] += 2
        elif inc_value == 'reset':
            return redirect('/')
        else:
            return "ERROR"
        return redirect('/success')
    else:
        return "ERROR"
    return redirect('/')


@app.route('/success')
def success():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
