from flask import Blueprint, render_template, request
from user.forms import RegisterForm, LoginForm

user_bp = Blueprint("users", __name__, url_prefix="/user")


@user_bp.route("/")
def main():
    reg_url = "<br><a href='/user/register'>Зарегистрироваться</a><br>"
    login_url = "<a href='/user/login'>Логин</a><br>"
    return f"Добро пожаловать на наш сайт {reg_url + login_url}"


user = []


@user_bp.route("/register", methods=['GET', 'POST'])
def root_register():
    form = RegisterForm()
    print("register")
    if request.method == "POST":
        if form.validate_on_submit():
            print("register")
            name = form.name.data
            email = form.email.data
            user.append(name)
            user.append(email)
            print(user)
            return "Регистрация прошла успешно"

    return render_template("register.html", form=form)


@user_bp.route("/login")
def root_login():
    form = LoginForm()

    return render_template("login.html", form=form)
