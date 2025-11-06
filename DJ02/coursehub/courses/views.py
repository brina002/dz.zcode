"""
Views for courses app.
"""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница CourseHub"""
    return render(request, 'index.html')


def catalog(request):
    """Страница каталога курсов"""
    return render(request, 'catalog.html')


def about(request):
    """Страница о нас"""
    return render(request, 'about.html')


def data_page(request):
    """Страница с данными и статистикой"""
    return render(request, 'data.html')


# Старая view-функция для совместимости
def test_page(request):
    """Тестовая страница для проверки функционала"""
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CourseHub - Тестирование</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }
                .container {
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                }
                h1 {
                    color: #667eea;
                    text-align: center;
                }
                .success {
                    color: #28a745;
                    font-weight: bold;
                }
                .info {
                    background: #e8f4f8;
                    padding: 20px;
                    border-radius: 8px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🧪 Тестирование CourseHub</h1>
                <p class="success">✓ Все маршруты работают корректно!</p>
                <div class="info">
                    <h3>Доступные страницы:</h3>
                    <ul>
                        <li><a href="/">Главная</a></li>
                        <li><a href="/catalog/">Каталог курсов</a></li>
                        <li><a href="/about/">О нас</a></li>
                        <li><a href="/data/">Данные</a></li>
                    </ul>
                    <p><strong>Урок 2 успешно выполнен!</strong></p>
                </div>
            </div>
        </body>
        </html>
    """)