from .db importname
class Size(db.Model):
    __tablename__ = "sizes"
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(45), nullable=True)

    products = db.relationship('Product', back_populates='sizes')

    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "products": self.products.to_dict(),
            }
