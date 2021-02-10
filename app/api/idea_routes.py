from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.models import db, Idea, Dap


idea_routes = Blueprint('ideas', __name__)


@idea_routes.route('')
def get_all_ideas():
    ideas = Idea.query.order_by(desc(Idea.id)).all()
    data = [idea.to_dict() for idea in ideas]
    return jsonify(data)


@idea_routes.route('/<ideaId>')
def get_all_daps_by_idea(ideaId):
    daps = Dap.query.filter(Dap.idea_id == ideaId).all()
    data = [dap.to_dict() for dap in daps]
    return jsonify(data)


@idea_routes.route("/create", methods=['POST'])
def create_idea():
    newIdea = Idea()
    newIdea.title = request.get_json().get("title")
    newIdea.user_id = request.get_json().get("user_id")
    newIdea.description = request.get_json().get("description")
    # data = request.json

    # idea = Idea(title=data["title"],user_id=data["user_id"], description=data["description"])
    db.session.add(newIdea)
    db.session.commit()
    return newIdea.to_dict()

@idea_routes.route('/<int:id>', methods=['DELETE'])
def delete_idea(id):
    idea = Idea.query.get(id)

    db.session.delete(idea)
    db.session.commit()

    return "Success it was deleted"


@idea_routes.route("/<int:id>", methods=["POST"])
def add_daps(id):
    newDap = Dap()
    newDap.user_id = request.get_json().get("user_id")
    newDap.idea_id = request.get_json().get("idea_id")

    db.session.add(newDap)
    db.session.commit()
    dapByIdea = Dap.query.filter(Dap.idea_id == request.get_json().get("idea_id")).all()
    data = [dap.to_dict() for dap in dapByIdea]

    return jsonify(data)
