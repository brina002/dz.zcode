"""
Views for courses app.
"""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница CourseHub"""
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CourseHub - Главная</title>
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
                    margin-bottom: 10px;
                }
                .subtitle {
                    text-align: center;
                    color: #666;
                    margin-bottom: 30px;
                }
                nav {
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 30px;
                    text-align: center;
                }
                nav a {
                    color: #667eea;
                    text-decoration: none;
                    margin: 0 15px;
                    font-weight: bold;
                    transition: color 0.3s;
                }
                nav a:hover {
                    color: #764ba2;
                }
                .content {
                    line-height: 1.8;
                    color: #333;
                }
                .features {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    margin-top: 30px;
                }
                .feature {
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    border-left: 4px solid #667eea;
                }
                .feature h3 {
                    color: #667eea;
                    margin-top: 0;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎓 CourseHub</h1>
                <p class="subtitle">Платформа онлайн-обучения</p>

                <nav>
                    <a href="/">Главная</a>
                    <a href="/data/">Данные</a>
                    <a href="/test/">Тестирование</a>
                </nav>

                <div class="content">
                    <h2>Добро пожаловать в CourseHub!</h2>
                    <p>
                        CourseHub — это современная платформа для онлайн-обучения, где вы можете 
                        найти курсы по различным направлениям, изучать новые навыки и развиваться 
                        профессионально.
                    </p>

                    <div class="features">
                        <div class="feature">
                            <h3>📚 Широкий выбор курсов</h3>
                            <p>Тысячи курсов по программированию, дизайну, маркетингу и другим направлениям.</p>
                        </div>
                        <div class="feature">
                            <h3>👨‍🏫 Опытные преподаватели</h3>
                            <p>Учитесь у профессионалов с многолетним опытом работы в индустрии.</p>
                        </div>
                        <div class="feature">
                            <h3>🎯 Гибкое обучение</h3>
                            <p>Занимайтесь в удобное время и в комфортном для вас темпе.</p>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
    """)


def data_page(request):
    """Страница с данными о курсах"""
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CourseHub - Данные</title>
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
                nav {
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 30px;
                    text-align: center;
                }
                nav a {
                    color: #667eea;
                    text-decoration: none;
                    margin: 0 15px;
                    font-weight: bold;
                }
                nav a:hover {
                    color: #764ba2;
                }
                .stats {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin: 30px 0;
                }
                .stat-card {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                }
                .stat-number {
                    font-size: 48px;
                    font-weight: bold;
                    margin: 10px 0;
                }
                .stat-label {
                    font-size: 14px;
                    opacity: 0.9;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }
                th {
                    background-color: #667eea;
                    color: white;
                }
                tr:hover {
                    background-color: #f5f5f5;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📊 Статистика и данные CourseHub</h1>

                <nav>
                    <a href="/">Главная</a>
                    <a href="/data/">Данные</a>
                    <a href="/test/">Тестирование</a>
                </nav>

                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-label">Всего курсов</div>
                        <div class="stat-number">247</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Студентов</div>
                        <div class="stat-number">5,432</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Преподавателей</div>
                        <div class="stat-number">89</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Отзывов</div>
                        <div class="stat-number">1,256</div>
                    </div>
                </div>

                <h2>Популярные категории курсов</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Категория</th>
                            <th>Количество курсов</th>
                            <th>Студентов</th>
                            <th>Средний рейтинг</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Программирование</td>
                            <td>87</td>
                            <td>2,341</td>
                            <td>⭐ 4.8</td>
                        </tr>
                        <tr>
                            <td>Дизайн</td>
                            <td>54</td>
                            <td>1,567</td>
                            <td>⭐ 4.7</td>
                        </tr>
                        <tr>
                            <td>Маркетинг</td>
                            <td>42</td>
                            <td>892</td>
                            <td>⭐ 4.6</td>
                        </tr>
                        <tr>
                            <td>Бизнес</td>
                            <td>38</td>
                            <td>456</td>
                            <td>⭐ 4.5</td>
                        </tr>
                        <tr>
                            <td>Языки</td>
                            <td>26</td>
                            <td>176</td>
                            <td>⭐ 4.9</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    """)


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
                nav {
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 30px;
                    text-align: center;
                }
                nav a {
                    color: #667eea;
                    text-decoration: none;
                    margin: 0 15px;
                    font-weight: bold;
                }
                nav a:hover {
                    color: #764ba2;
                }
                .test-section {
                    background: #f8f9fa;
                    padding: 20px;
                    margin: 20px 0;
                    border-radius: 8px;
                    border-left: 4px solid #667eea;
                }
                .test-item {
                    margin: 15px 0;
                    padding: 15px;
                    background: white;
                    border-radius: 5px;
                }
                .status {
                    display: inline-block;
                    padding: 5px 15px;
                    border-radius: 20px;
                    font-size: 12px;
                    font-weight: bold;
                }
                .status-success {
                    background: #28a745;
                    color: white;
                }
                .status-warning {
                    background: #ffc107;
                    color: #333;
                }
                .status-info {
                    background: #17a2b8;
                    color: white;
                }
                .code-block {
                    background: #2d2d2d;
                    color: #f8f8f2;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                    font-family: 'Courier New', monospace;
                    margin: 10px 0;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🧪 Тестирование системы CourseHub</h1>

                <nav>
                    <a href="/">Главная</a>
                    <a href="/data/">Данные</a>
                    <a href="/test/">Тестирование</a>
                </nav>

                <div class="test-section">
                    <h2>Проверка маршрутов (URLs)</h2>

                    <div class="test-item">
                        <strong>Главная страница:</strong> <span class="status status-success">✓ Работает</span>
                        <div class="code-block">path('', views.index, name='index')</div>
                    </div>

                    <div class="test-item">
                        <strong>Страница данных:</strong> <span class="status status-success">✓ Работает</span>
                        <div class="code-block">path('data/', views.data_page, name='data')</div>
                    </div>

                    <div class="test-item">
                        <strong>Тестовая страница:</strong> <span class="status status-success">✓ Работает</span>
                        <div class="code-block">path('test/', views.test_page, name='test')</div>
                    </div>
                </div>

                <div class="test-section">
                    <h2>Проверка приложения</h2>

                    <div class="test-item">
                        <strong>Приложение 'courses':</strong> <span class="status status-success">✓ Зарегистрировано</span>
                        <p>Приложение успешно добавлено в INSTALLED_APPS</p>
                    </div>

                    <div class="test-item">
                        <strong>Views функции:</strong> <span class="status status-success">✓ Созданы</span>
                        <p>Все необходимые view-функции определены и работают корректно</p>
                    </div>
                </div>

                <div class="test-section">
                    <h2>Следующие шаги</h2>

                    <div class="test-item">
                        <strong>Урок 2:</strong> <span class="status status-warning">⏳ В ожидании</span>
                        <p>Добавление шаблонизатора Jinja и Bootstrap стилей</p>
                    </div>

                    <div class="test-item">
                        <strong>Урок 3:</strong> <span class="status status-info">📋 Запланировано</span>
                        <p>Создание моделей для курсов и работа с базой данных</p>
                    </div>
                </div>

                <div style="margin-top: 30px; padding: 20px; background: #e8f4f8; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-top: 0;">💡 Информация о проекте</h3>
                    <p><strong>Проект:</strong> CourseHub</p>
                    <p><strong>Django версия:</strong> 4.x+</p>
                    <p><strong>Текущий урок:</strong> Урок 1 - Основы Django</p>
                    <p><strong>Статус:</strong> Базовая структура создана ✓</p>
                </div>
            </div>
        </body>
        </html>
    """)