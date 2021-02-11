from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.models import db,Dap, User, Idea


dap_routes = Blueprint('daps', __name__)


@dap_routes.route('/<int:userId>')
def get_all_daps_by_user(userId):
    daps = Dap.query.filter(Dap.user_id == userId).all()
    data = [dap.to_dict() for dap in daps]
    return jsonify(data)


@dap_routes.route('')
def get_all_daps():
    daps = Dap.query.all()
    data = [dap.to_dict() for dap in daps]
    return jsonify(data)


@dap_routes.route('/<int:ideaId>', methods=["POST"])
def delete_daps(ideaId):
    userId = request.get_json().get("user_id")
    dap = Dap.query.filter(Dap.user_id == userId).filter(Dap.idea_id == ideaId).first()
    db.session.delete(dap)
    # print("HERE IS THE DAPPPPPPPPPPPPP", dap)
    db.session.commit()

    dapByIdea = Dap.query.filter(Dap.idea_id == request.get_json().get("idea_id")).all()
    data = [dap.to_dict() for dap in dapByIdea]

    return jsonify(data)
