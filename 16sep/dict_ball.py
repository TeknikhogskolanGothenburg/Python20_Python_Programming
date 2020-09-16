import pygame
from random import randrange, choice

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, GREEN, YELLOW, PURPLE, CYAN]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
LOWEST_SPEED = 2
HIGHEST_SPEED = 10
BALL_RADIUS = 5
STARTING_POSITION = {'X': SCREEN_WIDTH // 2, 'Y': SCREEN_HEIGHT // 2}


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    number_of_balls = 6     # randrange(1, 6)
    ball_list = []

    for i in range(number_of_balls):
        ball_list.append(
            {
                'Color': COLORS[i],
                'Position': {'x': STARTING_POSITION['X'], 'y': STARTING_POSITION['Y']},
                'Direction': {'x': choice((-1, 1)), 'y': choice((-1, 1))},
                'Speed': {'x': random_speed(), 'y': random_speed()},
                'Radius': randrange(2, 10)
            }
        )

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        for i, ball in enumerate(ball_list):
            pygame.draw.circle(screen, ball['Color'], (ball['Position']['x'], ball['Position']['y']), ball['Radius'] * 2)
            ball_list[i] = update_position(ball)

        pygame.display.update()
        clock.tick(FPS)


def update_position(ball):
    if ball['Position']['x'] >= (SCREEN_WIDTH - ball['Radius'] - ball['Speed']['x']) or \
            ball['Position']['x'] <= (ball['Radius'] + ball['Speed']['x']):
        ball['Direction']['x'] *= -1
        ball['Speed']['x'] = random_speed()

    if ball['Position']['y'] >= (SCREEN_HEIGHT - ball['Radius'] - ball['Speed']['y']) or \
            ball['Position']['y'] <= (ball['Radius'] + ball['Speed']['y']):
        ball['Direction']['y'] *= -1
        ball['Speed']['y'] = random_speed()

    ball['Position']['x'] += ball['Speed']['x'] * ball['Direction']['x']
    ball['Position']['y'] += ball['Speed']['y'] * ball['Direction']['y']
    return ball


def random_speed():
    return randrange(LOWEST_SPEED, HIGHEST_SPEED)


if __name__ == '__main__':
    main()
