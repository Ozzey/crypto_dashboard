from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, validators, ValidationError
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash


from models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=5)
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')



class PortfolioForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Buy')


class SellForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Sell')
