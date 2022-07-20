from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo

class RegisterForm(Form):
    name = StringField('Name', validators=[
        InputRequired(),
        Length(min=1, max=50),
        
    ])
    username = StringField('Username', validators=[
        InputRequired(),
        Length(min=1, max=50),
       
    ])
    email = StringField('Email', validators=[InputRequired(),Length(min=6 , max=50)])
    password = PasswordField('Password', validators=[
        InputRequired(),
        DataRequired(),
        EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password', validators=[
        InputRequired(),
        EqualTo('password', message='Password do not match')
    ])
