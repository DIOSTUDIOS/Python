from flask_login import UserMixin
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from shortuuid import uuid


class User(db.Model, UserMixin):
    id = db.Column(db.String(20), primary_key=True, unique=False, default=uuid)
    name = db.Column(db.String(99), unique=False)
    username = db.Column(db.String(99), unique=True)
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Movie(db.Model):
    id = db.Column(db.String(20), primary_key=True, unique=False, default=uuid)
    title = db.Column(db.String(99), unique=False)
    year = db.Column(db.String(4))
