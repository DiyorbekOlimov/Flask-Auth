import os
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

database_path = os.environ.get('DATABASE_URL')

db = SQLAlchemy()

def create_db(app=None):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    return db


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    token = Column(String(), nullable=False)

    def __init__(self, name, email, password, token):
        self.name = name
        self.email = email
        self.password = password
        self.token = token

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
