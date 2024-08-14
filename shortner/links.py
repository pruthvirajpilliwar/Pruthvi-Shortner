from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_required, current_user
from .models import db, Link


bp = Blueprint("links", __name__)


from string import ascii_letters, digits
from random import choices

def generate_random_slug(length=7):
    return "".join(choices(ascii_letters+digits, k=length))

def generate_unique_slug(new_slug, old_slug):
    while new_slug == old_slug:
        new_slug = generate_random_slug()
    return new_slug



@bp.route("/links", methods=["GET", "POST"])
@login_required
def links():
    if request.method == "POST":
        url = request.form.get("url")

        new_slug = generate_random_slug()
        shortlink  = Link.query.filter_by(slug=new_slug).first()
        if shortlink:
            while new_slug == shortlink.slug:
                new_slug = generate_random_slug(7)

        new_shortlink = Link(url=url, slug=new_slug, user_id=current_user.id)
        db.session.add(new_shortlink)
        db.session.commit()

        flash("Shortlink created successfully!", category="success")
        return render_template("links.html", user=current_user)

    if not current_user.shortlinks:
        return "No links found"

    return render_template("links.html", user=current_user)
