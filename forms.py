from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ShowSearchForm(FlaskForm):
  show_name = StringField("Enter the name of a show: ", validators=[DataRequired()])
  submit = SubmitField("Jump the shark!")
