from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required,  current_user, logout_user, login_user, current_user

from . import db
from .models import User


bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    next = request.args.get("next", "/")

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", "success")
                login_user(user, remember=remember)
                return redirect(next)
        flash("Invalid login credentials", "danger")

    return render_template("signin.html", user=current_user)


@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "success")

    return redirect(url_for('auth.login'))


@bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print(email, password1, password2)

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Account already exists", "warning")
            return redirect(url_for('auth.sign_up'))
        if len(email) < 5:
            flash("Enter valid email address", "danger")
            return redirect(url_for('auth.sign_up'))
        if len(password1) < 8 or len(password1) > 21:
            flash("Your password must be 8-20 characters long.", "danger")
            return redirect(url_for('auth.sign_up'))
        if password1 != password2:
            flash("Password & confirm password not matched", "danger")
            return redirect(url_for('auth.sign_up'))

        new_user = User(email=email, password=generate_password_hash(password=password1, method="pbkdf2:sha256"))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash("Account created succesfully!", category="success")
        return redirect(url_for('home.home'))

    return render_template("register.html", user=current_user)
