from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import current_user
from .models  import db, Link

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
def home():
    return render_template("home.html", user=current_user)


@bp.route("/<string:slug>")
def link_redirect(slug):
    shortlink = Link.query.filter_by(slug=slug).first()
    if not shortlink:
        flash("Invalid link", category="danger")
        return redirect(url_for("home.home"))

    shortlink.clicks += 1
    db.session.commit()

    return redirect(shortlink.url)
