from .db import db


class Dap(db.Model):
    __tablename__ = "daps"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    idea_id = db.Column(db.Integer, db.ForeignKey('ideas.id'), nullable=True)


    def to_dict(self):
            return {
                "id": self.id,
                "user_id": self.user_id,
                "idea_id": self.idea_id,


                # "amenities": [x.to_dict() for x in self.amenities]
            }
