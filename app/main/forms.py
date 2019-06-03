from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField('Type',choices=[('Product','Product'), ('Business','Business'), ('Tech','Tech')],validators=[Required()])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Talk to us.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comments = TextAreaField('comments', validators=[Required()])
    submit = SubmitField('Submit Comment')