from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo('password')])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class StudentForm(FlaskForm):
    roll = IntegerField("Roll Number", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    gender = SelectField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    subject = SelectField("Subject", choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Math', 'Math'), ('English', 'English')])
    marks = IntegerField("Marks", validators=[DataRequired()])
    submit = SubmitField("Add / Update Student")
