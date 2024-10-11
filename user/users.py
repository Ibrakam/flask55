from flask import Blueprint, render_template
from user.forms import RegisterForm, LoginForm

user_bp = Blueprint("users", __name__, url_prefix="/user")


@user_bp.route("/")
def main():
    reg_url = "<br><a href='/user/register'>Зарегистрироваться</a><br>"
    login_url = "<a href='/user/login'>Логин</a><br>"
    return f"Добро пожаловать на наш сайт {reg_url + login_url}"


@user_bp.route("/register")
def root():
    form = RegisterForm()

    return render_template("register.html", form=form)



