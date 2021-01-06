from .db import db


class OrderDetail(db.Models):
    __tablename__ - "orderDetails"
    id = db.Column(db.Integer, primary_key=True nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)

    products = db.relationship('Product', backpopulates='orderDetails')
    orders = db.relationship('Order', backpopulates='products')
