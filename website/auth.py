from xmlrpc.client import boolean
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Filter all the user with this specific email
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.')
        else:
            flash('Email does not exist.')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.',)
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.',)
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.')
        elif password1 != password2:
            flash('Passwords do not match.')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters.')
        else:
            # create a new user
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user) # add the new user to the database
            db.session.commit() # update the database
            login_user(user, remember=True)
            flash('Account successfully created!')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)