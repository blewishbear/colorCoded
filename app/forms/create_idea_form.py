from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Idea



class CreateIdeaForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
