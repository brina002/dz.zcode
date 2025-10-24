from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from app.models import User

class RegistrationForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(1, 120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(1, 120)])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField("Повторите пароль", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("Пользователь с таким email уже существует.")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(1, 120)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")

class UpdateAccountForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(1, 120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(1, 120)])
    password = PasswordField("Новый пароль", validators=[Optional(), Length(min=6)])
    password2 = PasswordField("Повторите пароль", validators=[Optional(), EqualTo('password')])
    submit = SubmitField("Сохранить")

    def __init__(self, original_email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_email = original_email

    def validate_email(self, field):
        if field.data.lower() != self.original_email:
            if User.query.filter_by(email=field.data.lower()).first():
                raise ValidationError("Этот email уже используется другим пользователем.")
