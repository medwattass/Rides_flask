from flask import render_template, session,redirect, request,flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
bcrypt = Bcrypt(app)


#===================Redirecting to the Login page==============================
@app.route('/')
def index():
    return redirect('/log_page')


#===================Redirecting to the Login page==============================
@app.route('/log_page')
def log_page():
    return render_template('login.html')


#===================Redirecting to the Registration page==============================
@app.route('/registration')
def reg_page():
    return render_template('registration.html')


#===================Registration method==============================
@app.route('/register',methods=['POST'])
def register():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect('/registration')
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(new_user)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')


#===================Login method==============================
@app.route("/login",methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect('/log_page')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect('/log_page')
    session['user_id'] = user.id
    return redirect('/dashboard')

