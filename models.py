"""Models for Cupcake app."""

"""Database Setup"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Initiates a connection to the DB"""
    db.app = app
    db.init_app(app)
    db.create_all()


class Cupcake(db.Model):
    __tablename__ = 'cupcakes'
    
    DEFAULT_IMAGE_URL = 'https://tinyurl.com/demo-cupcake'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, server_default=DEFAULT_IMAGE_URL)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    