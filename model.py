from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationship: one user has many todos
    todos = db.relationship('Todo', backref='user', lazy=True)

# Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='Not Completed')
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
