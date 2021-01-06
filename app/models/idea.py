from .db import db

class Idea(db.Models):
    __tablename__ = "ideas"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, , nullable=False)
    created_at = db.Column(db.DateTime, , nullable=False)
    updated_at = db.Column(db.DateTime, , nullable=False)

    owner = db.relationship('User', backpopulates='ideas')
    daps = db.relationship('Dap', backpopulates='ideas')
