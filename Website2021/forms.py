from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, ValidationError
import models


class Add_Review(FlaskForm):
  name = TextField('Name', validators=[DataRequired()])
  rating = IntegerField('Rating', validators=[DataRequired()])
  comment = TextField('Description', validators=[DataRequired()])
  submit = SubmitField('Save')
