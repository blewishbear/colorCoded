from .db import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(55), nullable=True)

    products = db.relationship('Product', back_populates='categories')

    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "products": self.products.to_dict(),
            }
