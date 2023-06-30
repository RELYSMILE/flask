from flask import Flask, render_template, redirect,request,session, url_for,flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hi'
app.permanent_session_lifetime = timedelta(hours=1)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/loginPage', methods =['POST', 'GET'])
def login():
    session.permanent = True
    if request.method == 'POST':
        user = request.form['name']
        session['user'] = user
        if 'user' in session:
            return redirect(url_for('home'))
    else:
        if 'user' in session:
            return redirect(url_for('home'))  
    return render_template('login.html')

@app.route('/homePage')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('homepage.html')

@app.route('/update', methods =['POST', 'GET'])
def Update():
    if request.method == 'POST':
        email = request.form['email']
        session['email'] = email
        if 'email' in session:
            return redirect(url_for('home'))
    return render_template('profile.html')


@app.route('/logout')
def Logout():
    flash('logout successfully!')
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')