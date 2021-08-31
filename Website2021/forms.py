from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, SubmitField,Form, BooleanField, StringField,FileField, PasswordField, validators, TextAreaField,ValidationError
from wtforms.validators import DataRequired, Optional, ValidationError


class Add_Review(FlaskForm):
  name = StringField('Name', [validators.Length(min=2, max=25)])
  rating = IntegerField('Rating', [validators.NumberRange(min=0, max=5)])
  comment = StringField('Comment', [validators.Length(min=2, max=250)])
  submit = SubmitField('Save')
