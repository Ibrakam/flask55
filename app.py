from flask import Flask, render_template, request

from admin import admin_bp
from user.users import user_bp

# создаем объект
app = Flask(__name__)

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'lksdkljas'

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")


@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        front_question = request.form.get("question")
        front_main_text = request.form.get("main_text")
        print(front_question)
        print(front_main_text)
        return render_template("add_question.html")
    else:
        return render_template("index.html")


app.run(debug=True)
