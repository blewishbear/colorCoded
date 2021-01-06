from .db import db
from .product import product_orders


class Order(db.Models):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, , nullable=False)
    updated_at = db.Column(db.DateTime, , nullable=False)


products = db.relationship('Product', secondary=product_orders, backpopulates='orders')
