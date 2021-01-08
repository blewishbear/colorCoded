from .db import db


class OrderDetail(db.Model):
    __tablename__ - "orderDetails"
    id = db.Column(db.Integer, primary_key=True nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)

    products = db.relationship('Product', back_populates='orderDetails')
    orders = db.relationship('Order', back_populates='products')

     def to_dict(self):
            return {
                "id": self.id,
                "product_id": self.product_id,
                "title": self.title,
                "order_id": self.order_id,
                "quantity": self.quantity,
                "products": self.products.to_dict(),
                "orders": self.orders.to_dict(),
                # "amenities": [x.to_dict() for x in self.amenities]
            }
