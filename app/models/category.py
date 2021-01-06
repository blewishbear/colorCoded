from .db import db


class Category(db.Models):
    __tablename__ - "categories"
    id = db.Column(db.Integer, primary_key=True nullable=True)
    category_name = db.Column(db.String(55), nullable=True)

    products = db.relationship('Product', backpopulates='categories')
