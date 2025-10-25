from flask import Flask, render_template
import requests

app = Flask(__name__)

# 🔑 Укажи свой API ключ от api-ninjas.com
API_KEY = "Nf904DLztawIrZ7zpRv4kQ==ud84hQoVBJ4vKs87"

@app.route("/")
def index():
    url = "https://api.api-ninjas.com/v1/quotes"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()[0]  # Берём первую цитату из списка
        quote = data["quote"]
        author = data["author"]
    except Exception as e:
        quote = "Не удалось получить цитату 😔"
        author = str(e)

    return render_template("index.html", quote=quote, author=author)

if __name__ == "__main__":
    app.run(debug=True)
