from .db import db


class Dap(db.Models):
    __tablename__ - "daps"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id') nullable=True)
    idea_id = db.Column(db.Integer, db.ForeignKey('ideas.id') nullable=True)

    owner = db.relationship('User', backpopulates='daps')
    idea = db.relationship('User', backpopulates='daps')
