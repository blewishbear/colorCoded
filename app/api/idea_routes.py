from flask import Blueprint, jsonify

from app.models import Idea


idea_routes = Blueprint('ideas', __name__)


@idea_routes.route('/')
def get_all_ideas():
    ideas = Idea.query.all()
    data = [idea.to_dict() for idea in ideas]
    return jsonify(data)
