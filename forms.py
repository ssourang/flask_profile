from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactMeForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    content = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Contact Me")
