import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Game")

# Colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Shapes
SQUARE = "square"
TRIANGLE = "triangle"
CIRCLE = "circle"
SHAPES = [SQUARE, TRIANGLE, CIRCLE]

# Initialize game variables
score = 0
current_shape = random.choice(SHAPES)
current_color = random.choice([RED, YELLOW, BLUE])
shape_x = random.randint(50, WIDTH - 50)
shape_y = HEIGHT - 100

# Game loop
while True:
    t = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if current_shape == SQUARE and shape_x <= mouse_x <= shape_x + 50 and shape_y <= mouse_y <= shape_y + 50:
                score += 1
            elif current_shape == TRIANGLE and shape_x <= mouse_x <= shape_x + 50 and shape_y <= mouse_y <= shape_y + 50:
                score += 1
            elif current_shape == CIRCLE and pygame.math.Vector2(shape_x + 25, shape_y + 25).distance_to(pygame.math.Vector2(mouse_x, mouse_y)) <= 25:
                score += 1

            # Generate a new shape and color
            current_shape = random.choice(SHAPES)
            current_color = random.choice([RED, YELLOW, BLUE])
            shape_x = random.randint(50, WIDTH - 50)
            shape_y = HEIGHT - random.randint(100, 500)
    if(t==50000):
        break
    screen.fill((0, 0, 0))  # Clear the screen

    # Draw the current shape
    if current_shape == SQUARE:
        pygame.draw.rect(screen, current_color, (shape_x, shape_y, 50, 50))
    elif current_shape == TRIANGLE:
        pygame.draw.polygon(screen, current_color, [(shape_x, shape_y + 50), (shape_x + 25, shape_y), (shape_x + 50, shape_y + 50)])
    elif current_shape == CIRCLE:
        pygame.draw.circle(screen, current_color, (shape_x + 25, shape_y + 25), 25)

    # Display score
    imp = pygame.image.load("icon.jpeg").convert()
    screen.blit(imp, (200, 200))
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    pygame.display.flip()