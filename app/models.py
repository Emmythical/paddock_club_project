from datetime import datetime
from flask_login import UserMixin
from . import db


class User(db.Model):
    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    __tablename__="Post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
