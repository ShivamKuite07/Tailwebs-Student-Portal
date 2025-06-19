from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, Teacher
from forms import SignupForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing = Teacher.query.filter_by(email=form.email.data).first()
        if existing:
            flash("Email already registered.", "warning")
            return redirect(url_for('auth.signup'))

        hashed_pw = generate_password_hash(form.password.data)
        teacher = Teacher(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(teacher)
        db.session.commit()
        flash("Signup successful. Please log in.", "success")
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        teacher = Teacher.query.filter_by(email=form.email.data).first()
        if teacher and check_password_hash(teacher.password, form.password.data):
            login_user(teacher)
            return redirect(url_for('student.dashboard'))
        flash("Invalid email or password.", "danger")
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for('auth.login'))
