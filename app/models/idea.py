from .db import db

class Idea(db.Model):
    __tablename__ = "ideas"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    user = db.relationship('User', back_populates='ideas')

    daps = db.relationship(
        "Dap", back_populates='idea', cascade="all, delete-orphan")


    def to_dict(self):
            return {
                "id": self.id,
                "user_id": self.user_id,
                "title": self.title,
                "description": self.description,
                "user": self.user.to_shall_dict(),

                # "amenities": [x.to_dict() for x in self.amenities]
            }
