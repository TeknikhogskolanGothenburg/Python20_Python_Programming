import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    running = True
    y = 300

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (400, y), 10)

        pygame.display.update()
        y += 2
        clock.tick(FPS)

if __name__ == '__main__':
    main()
