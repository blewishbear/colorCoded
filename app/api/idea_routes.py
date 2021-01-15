from flask import Blueprint, jsonify, request

from app.models import db, Idea


idea_routes = Blueprint('ideas', __name__)


@idea_routes.route('/')
def get_all_ideas():
    ideas = Idea.query.all()
    data = [idea.to_dict() for idea in ideas]
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
