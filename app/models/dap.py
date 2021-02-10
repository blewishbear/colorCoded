from .db import db


class Dap(db.Model):
    __tablename__ = "daps"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    idea_id = db.Column(db.Integer, db.ForeignKey('ideas.id'), nullable=True)

    idea = db.relationship(
        "Idea",  back_populates="daps")

    user = db.relationship(
        "User",  back_populates="daps")


    def to_dict(self):
            return {
                "id": self.id,
                "user": self.user.to_dict(),
                "idea": self.idea.to_dict(),


                # "amenities": [x.to_dict() for x in self.amenities]
            }
