from .db import db
from .product import product_orders


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    


    products = db.relationship('Product', secondary=product_orders, back_populates='orders')
    users = db.relationship("User", back_populates="orders")

    def to_dict(self):
            return {
            "id": self.id,
            "user_id": self.user_id.to_dict(),
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "products": self.products.to_dict(),
            }
