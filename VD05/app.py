from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return render_template("home.html")

# О проекте
@app.route("/about")
def about():
    return render_template("about.html")

# 1️⃣ Тестирование методов запоминания
@app.route("/methods", methods=["GET", "POST"])
def methods():
    result = None
    if request.method == "POST":
        method = request.form.get("method")
        word = request.form.get("word")
        # Простая имитация "эффективности" (в реальности тут можно хранить статистику)
        result = f"Метод '{method}' для слова '{word}' показал эффективность {len(word) * 10}%"
    return render_template("methods.html", result=result)

# 2️⃣ A/B-тестирование техник
@app.route("/ab-test", methods=["GET", "POST"])
def ab_test():
    result = None
    if request.method == "POST":
        group = request.form.get("group")
        score = int(request.form.get("score", 0))
        feedback = "A" if score > 50 else "B"
        result = f"Вы в группе {group}. Эффективнее оказалась техника: {feedback}"
    return render_template("ab_test.html", result=result)

# 3️⃣ Персонализированные планы обучения
@app.route("/plan", methods=["GET", "POST"])
def plan():
    plan = None
    if request.method == "POST":
        level = request.form.get("level")
        time = int(request.form.get("time"))
        if time < 30:
            plan = "Короткие 10-минутные сессии с карточками и повторением."
        else:
            plan = "Полноценные 30–45-минутные занятия с тестами и визуализацией."
    return render_template("plan.html", plan=plan)

# 4️⃣ Ассоциативные цепочки
@app.route("/associations", methods=["GET", "POST"])
def associations():
    associations = None
    if request.method == "POST":
        word = request.form.get("word")
        base_associations = {
            "sun": ["light", "warm", "day", "energy"],
            "book": ["read", "knowledge", "library", "story"],
            "tree": ["leaf", "green", "forest", "life"]
        }
        associations = base_associations.get(word.lower(), ["Нет данных — добавьте свои ассоциации!"])
    return render_template("associations.html", associations=associations)

if __name__ == "__main__":
    app.run(debug=True)
