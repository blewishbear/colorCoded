from flask import Blueprint, jsonify

from app.models import Product

product_routes = Blueprint('t-shirts', __name__)


@product_routes.route('/')
def get_all_products():
    products = Product.query.all()
    data = [product.to_dict() for product in products]
    return jsonify(data)
# @product_routes.route('/<int:color_id>/<int:size_id>')
# def get_all_products_by_color(color_id, size_id):
#     products = Product.query.filter_by(color_id=color_id, size_id=size_id )
#     data = [product.to_dict() for product in products]
#     return jsonify(data)


@product_routes.route('/<int:id>')
def get_one_product(id):
    product = Product.query.get(id)
    images = product.images

    return {"product":product.to_dict(),
            "images": images}
