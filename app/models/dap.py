from .db import db


class Dap(db.Model):
    __tablename__ = "daps"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    idea_id = db.Column(db.Integer, db.ForeignKey('ideas.id'), nullable=True)

    
