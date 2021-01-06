from .db import db


product_orders = db.Table('product_orders',
                    db.Integer,db.ForeignKey('products.id'),
                    primary_key=True),db.Column('order_id',
                    db.Integer,db.ForeignKey('orders.id'), primary_key=True)

class Product(db.Models):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    description = db.Column(db.Text, , nullable=False)
    price = db.Column(db.Integer, , nullable=False)
    color_id = db.Column(db.Integer, , nullable=False)
    size_id = db.Column(db.Integer, , nullable=False)
    stock = db.Column(db.Integer, , nullable=False)
    img_url = db.Column(db.Text, , nullable=False)




categories = db.relationship('Catergory', backpopulates='products')
color_id = db.relationship('Color', backpopulates='products')
size_id = db.relationship('Size', backpopulates='products')
orders = db.relationship('Order', secondary=product_orders backpopulates='products')
