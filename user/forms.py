from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired


# Форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired("Заполните имя")])
    email = EmailField("Почта", validators=[DataRequired("Заполните почту")])
    password = PasswordField("Пароль", validators=[DataRequired("Заполните пароль")])
    password2 = PasswordField("Повторить", validators=[DataRequired("Заполните пароль")])
    button = SubmitField("Зарегистрироваться")


# Форма для логина
class LoginForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired("Заполните почту")])
    password = PasswordField("Пароль", validators=[DataRequired("Заполните пароль")])
    button = SubmitField("Войти")
