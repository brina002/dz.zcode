import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Загрузка звуков
ball_hit_sound = pygame.mixer.Sound("C:/Users/Гузалина/Music/ping_pong_sounds/ball_hit_real.wav")
score_sound = pygame.mixer.Sound("C:/Users/Гузалина/Music/ping_pong_sounds/score_point_real.wav")
win_sound = pygame.mixer.Sound("C:/Users/Гузалина/Music/ping_pong_sounds/victory_sound.wav")

win_sound.set_volume(1.0)  # Устанавливаем громкость звука победы

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Настройки объектов
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 15

# Позиции ракеток
left_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2

# Скорости
paddle_speed = 5
ball_x_speed = 4
ball_y_speed = 4

# Счёт
left_score = 0
right_score = 0
max_score = 10  # Победа при 10 очках

# Частота обновления экрана
clock = pygame.time.Clock()
FPS = 60

# Шрифт
font = pygame.font.SysFont("Arial", 30)

# Флаг окончания игры
game_over_flag = False

# Функция завершения игры
def game_over(winner):
    global game_over_flag
    game_over_flag = True

    # Отображение текста победителя
    winner_text = f"{winner} победил!"
    winner_display = font.render(winner_text, True, WHITE)
    screen.fill(BLACK)
    screen.blit(winner_display, (WIDTH // 2 - winner_display.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    # Проигрывание звука победы
    win_sound.play()

    # Ожидание, чтобы звук успел проиграться
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

# Основной игровой цикл
def main():
    global left_paddle_y, right_paddle_y, ball_x, ball_y, ball_x_speed, ball_y_speed
    global left_score, right_score, game_over_flag

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Проверяем флаг окончания игры
        if game_over_flag:
            break

        # Управление ракетками
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle_y > 0:
            left_paddle_y -= paddle_speed
        if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
            left_paddle_y += paddle_speed
        if keys[pygame.K_UP] and right_paddle_y > 0:
            right_paddle_y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
            right_paddle_y += paddle_speed

        # Движение мяча
        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # Отражение мяча от стен
        if ball_y <= 0:  # Верхняя стенка
            ball_y_speed = -ball_y_speed

        if ball_y >= HEIGHT - BALL_SIZE:  # Нижняя стенка
            ball_y_speed = -ball_y_speed

        # Отражение мяча от ракеток
        if (ball_x <= PADDLE_WIDTH and left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT) or \
                (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT):
            ball_x_speed = -ball_x_speed
            ball_hit_sound.play()

        # Проверка выхода мяча за пределы
        if ball_x <= 0:  # Очко правому игроку
            right_score += 1
            ball_x = WIDTH // 2 - BALL_SIZE // 2
            ball_y = HEIGHT // 2 - BALL_SIZE // 2
            ball_x_speed = -ball_x_speed
            score_sound.play()

        if ball_x >= WIDTH - BALL_SIZE:  # Очко левому игроку
            left_score += 1
            ball_x = WIDTH // 2 - BALL_SIZE // 2
            ball_y = HEIGHT // 2 - BALL_SIZE // 2
            ball_x_speed = -ball_x_speed
            score_sound.play()

        # Проверка на победителя
        if left_score >= max_score:
            game_over("Игрок 1")
        elif right_score >= max_score:
            game_over("Игрок 2")

        # Отрисовка объектов
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

        # Отображение счёта
        left_score_text = font.render(f"Игрок 1: {left_score}", True, WHITE)
        right_score_text = font.render(f"Игрок 2: {right_score}", True, WHITE)
        screen.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
        screen.blit(right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width() // 2, 20))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
