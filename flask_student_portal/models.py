from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Teacher(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class StudentMark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(1), nullable=False)  # 'M' or 'F'
    subject = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.Integer, nullable=False)
