from .db import db


class Color(db.Models):
    __tablename__ - "colors"
    id = db.Column(db.Integer, primary_key=True nullable=True)
    name = db.Column(db.String(55), nullable=True)

    products = db.relationship('Product', backpopulates='colors')
