from App.ext import db


class Animal(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    a_name = db.Column(db.String(16))