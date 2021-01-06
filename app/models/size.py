from .db import db


class Size(db.Models):
    __tablename__ - "sizes"
    id = db.Column(db.Integer, primary_key=True nullable=True)
    name = db.Column(db.String(55), nullable=True)

    products = db.relationship('Product', backpopulates='sizes')
