from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo
from app.models import Contact

class MessageForm(FlaskForm):
  message = StringField('Message', validators=[DataRequired()])
  send_to = SelectField(choices=[(i.phone, i.name) for i in Contact.query.all()], validators=[DataRequired()])
  submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
  name = StringField('Full Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = StringField('Password', validators=[DataRequired()])
  password_2 = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Submit')

class AddContactForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  phone = IntegerField('Phone', validators=[DataRequired()])
  submit = SubmitField('Submit')