from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('main', __name__)

# Временное хранилище пользователей (в памяти)
users = []


@bp.route("/")
def home():
    return render_template("home.html", users=users)


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    city = request.form.get("city")
    hobby = request.form.get("hobby")
    age = request.form.get("age")

    # Валидация данных
    if not name or not city or not hobby or not age:
        flash("Пожалуйста, заполните все поля!", "warning")
        return redirect(url_for("main.home"))

    try:
        age = int(age)
        if age < 1 or age > 120:
            flash("Пожалуйста, введите корректный возраст!", "warning")
            return redirect(url_for("main.home"))
    except ValueError:
        flash("Возраст должен быть числом!", "warning")
        return redirect(url_for("main.home"))

    # Добавляем пользователя
    user = {
        "name": name,
        "city": city,
        "hobby": hobby,
        "age": age
    }
    users.append(user)

    flash(f"Пользователь {name} успешно добавлен!", "success")
    return redirect(url_for("main.home"))


@bp.route("/clear_users", methods=["POST"])
def clear_users():
    users.clear()
    flash("Все карточки удалены!", "info")
    return redirect(url_for("main.home"))