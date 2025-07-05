import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ game
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Tốc độ game (frame per second)
FPS = 10

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Game Con Rắn")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], CELL_SIZE, CELL_SIZE])

def show_score(score):
    value = font.render("Điểm: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    # Vị trí khởi đầu của rắn
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    # Tạo vị trí ngẫu nhiên cho "thức ăn"
    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Thua rồi! Nhấn Q để thoát, C để chơi lại", True, RED)
            screen.blit(msg, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -CELL_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = CELL_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -CELL_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = CELL_SIZE
                    x_change = 0

        x += x_change
        y += y_change

        # Kiểm tra va chạm tường
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)

        # Vẽ thức ăn
        pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        # Cập nhật thân rắn
        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        # Kiểm tra va chạm với chính mình
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake)
        show_score(snake_length - 1)

        pygame.display.update()

        # Ăn thức ăn
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()