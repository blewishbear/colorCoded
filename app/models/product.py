from .db import db


product_orders = db.Table('product_orders',
                    db.Column('products_id',db.Integer,db.ForeignKey('products.id'),
                    primary_key=True),db.Column('order_id',
                    db.Integer,db.ForeignKey('orders.id'), primary_key=True), extend_existing=True)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.Text, nullable=False)


    categories = db.relationship('Category', back_populates='products')
    colors = db.relationship('Color', back_populates='products')
    images = db.relationship('Color', back_populates='products')
    sizes = db.relationship('Size', back_populates='products')
    orders = db.relationship('Order', secondary=product_orders, back_populates='products')
    orderDetails = db.relationship('OrderDetail', back_populates="products")


    def to_dict(self):
            return {
                "id": self.id,
                "title": self.title,
                "category_id": self.category_id,
                "price": self.price,
                "color_id": self.color_id,
                "size_id": self.size_id,
                "stock": self.stock,
                "img_url": self.img_url,
                # "orders": self.orders.to_dict(),

            }
