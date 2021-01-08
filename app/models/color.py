from .db import db


class Color(db.Model):
    __tablename__ = "colors"
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(45), nullable=True)

    products = db.relationship('Product', back_populates='colors')


    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "products.to_dict()": self.products.to_dict(),
            }
