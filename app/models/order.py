from .db import db
from .product import product_orders


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)



    products = db.relationship('Product', secondary=product_orders, back_populates='orders')
    user = db.relationship("User", back_populates="orders")
    orderDetails = db.relationship("OrderDetail", back_populates="orders")

    def to_dict(self):
            return {
            "id": self.id,
            "user": self.user.to_dict()
            }
