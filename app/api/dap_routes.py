from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.models import db,Dap, User


dap_routes = Blueprint('daps', __name__)


@dap_routes.route('/<userId>')
def get_all_daps_by_user(userId):
    daps = Dap.query.filter(Dap.user_id == userId).all()
    data = [dap.to_dict() for dap in daps]
    return jsonify(data)


@dap_routes.route('/')
def get_all_daps():
    daps = Dap.query.all()
    data = [dap.to_dict() for dap in daps]
    return jsonify(data)
