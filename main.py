from flask import Flask, render_template, redirect,url_for,session,request

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/home')
def home():
    return render_template('home.html' , title = 'Home')

@app.route('/login' ,methods = ["POST" , "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        session["password"] = password
        session["email"] = email
    
    if "email" in session:
        return redirect(url_for('home'))
    return render_template('login.html' , title = 'Login')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)