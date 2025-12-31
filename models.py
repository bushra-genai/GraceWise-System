from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    
    # Relationship with DevotionalProgress
    # devotional_progress = db.relationship("DevotionalProgress", backref="user", cascade="all, delete-orphan")


# Child model
class Child(db.Model):
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)


# Devotional model
class Devotional(db.Model):
    __tablename__ = "devotional"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with DevotionalProgress
    progress = db.relationship("DevotionalProgress", backref="devotional", cascade="all, delete-orphan")


# DevotionalProgress model
class DevotionalProgress(db.Model):
    __tablename__ = "devotional_progress"

    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(
        db.Integer,
        db.ForeignKey("child.id"),
        nullable=False
    )
    devotional_id = db.Column(
        db.Integer,
        db.ForeignKey("devotional.id"),
        nullable=False
    )


# Planner model
class Planner(db.Model):
    __tablename__ = "planner"
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"), nullable=False)
    task_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(50), default="Pending")


# Curriculum model
class Curriculum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    age_group = db.Column(db.String(50))
    week = db.Column(db.Integer)
    devotional_id = db.Column(db.Integer, db.ForeignKey("devotional.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
