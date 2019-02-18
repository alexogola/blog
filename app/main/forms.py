from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email
from ..models import Subscriber
from wtforms import ValidationError

class BlogForm(FlaskForm):
    category = StringField('<p style="color: #d90600; padding: 0px; margin: 0px;">Post Sumn</p>' ,validators=[Required()])
    title = StringField('<p style="color: #d90600; padding: 0px; margin: 0px;">Enter Your Name<p>' ,validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = StringField('<p style="color: #d90600; padding: 0px; margin: 0px;">Write A comment</p>' ,validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('<p style="color: #d90600; padding: 0px; margin: 0px;">Tell us about you.</p>',validators = [Required()])
    submit = SubmitField('Submit')


class SubscriberForm(FlaskForm):
    email = StringField('<p style="color: #d90600; padding: 0px; margin: 0px;">Enter Email Address</p>',validators=[Required(),Email()])
    title = StringField('<p style="color: #d90600; padding: 0px; margin: 0px;">Enter Your Name</p>' ,validators=[Required()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
                if Subscriber.query.filter_by(email =data_field.data).first():
                    raise ValidationError('There is an account with that email')
