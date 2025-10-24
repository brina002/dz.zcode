from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, logout_user, current_user, login_required

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    users = User.query.all()
    return render_template("home.html", users=users)

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data.lower())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Регистрация прошла успешно. Войдите в систему.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Добро пожаловать, {user.name}!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.home"))
        flash("Неверный email или пароль.", "danger")
    return render_template("login.html", form=form)

@bp.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из системы.", "info")
    return redirect(url_for("main.home"))

@bp.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm(original_email=current_user.email)
    if request.method == "GET":
        # Предзаполнить поля текущими данными
        form.name.data = current_user.name
        form.email.data = current_user.email

    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data.lower()
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash("Профиль обновлён.", "success")
        return redirect(url_for("main.account"))
    return render_template("account.html", form=form)

# Optional: простой способ удалить всех пользователей (для dev)
@bp.route("/clear_users", methods=["POST"])
def clear_users():
    # Только если нет авторизации или разрешено — осторожно!
    User.query.delete()
    db.session.commit()
    flash("Все пользователи удалены (dev).", "info")
    return redirect(url_for("main.home"))
