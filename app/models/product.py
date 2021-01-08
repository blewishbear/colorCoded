from .db import db


product_orders = db.Table('product_orders',
                    db.Column('products_id',db.Integer,db.ForeignKey('products.id'),
                    primary_key=True),db.Column('order_id',
                    db.Integer,db.ForeignKey('orders.id'), primary_key=True))

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    color_id = db.Column(db.Integer, nullable=False)
    size_id = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.Text, nullable=False)


    categories = db.relationship('Catergory', back_populates='products')
    colors = db.relationship('Color', back_populates='products')
    sizes = db.relationship('Size', back_populates='products')
    orders = db.relationship('Order', secondary=product_orders, back_populates='products')


    def to_dict(self):
            return {
                "id": self.id,
                "title": self.title,
                "category_id": self.category_id,
                "price": self.price,
                "color_id": self.color_id,
                "size_id": self.size_id,
                "stock": self.stock
                "categories": self.categories..to_dict(),
                "colors": self.colors..to_dict(),
                "sizes": self.sizes..to_dict(),
                "orders": self.orders..to_dict(),
                # "amenities": [x.to_dict() for x in self.amenities]
            }
