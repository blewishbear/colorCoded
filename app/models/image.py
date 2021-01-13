from .db import db

class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    color_id = db.Column(db.String(45),db.ForeignKey('colors.id') nullable=False)
    img_url = db.Column(db.Text(255), nullable=False)

    products = db.relationship('Products', back_populates='images')
    colors = db.relationship('Color', back_populates='images')


    def to_dict(self):
            return {
                "id": self.id,
                "product_id": self.product_id,
                "img_url": self.img_url,
                "color_id": self.color_id,
                "colors": self.colors.to_dict(),
                "products": self.products.to_dict(),
                
            }
