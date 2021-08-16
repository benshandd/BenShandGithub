from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional, ValidationError
import models


class Add_Review(FlaskForm):
  name = TextField('name', validators=[DataRequired()])
  rating = IntegerField('rating', validators=[DataRequired()])
  comment = TextField('description', validators=[DataRequired()])


#class Select_Movie(FlaskForm):
 # movies = SelectField('movies', validators=[DataRequired()], coerce=int)
