from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(102), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    shortlinks = db.relationship('Link', backref='user', passive_deletes=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id} email={self.email})>"


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    slug = db.Column(db.String(30), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    clicks = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="cascade"), nullable=False)

    def __repr__(self) -> str:
        return f"<ShortLink(id={self.id} slug={self.slug})>"

