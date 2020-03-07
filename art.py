import pygame
from collections import namedtuple
from random import randint
import time
from itertools import cycle
pygame.init()


width, height = 1920, 1080
display = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

points = [(randint(0, width), randint(0, height)) for i in range(2)]
time_ = time.time()
rgb = cycle(
    [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
)
col = next(rgb)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    display.fill((0, 0, 0))

    for i in range(1, len(points) - 1):
        if time.time() >= time_ + 1:
            time_ = time.time()
            col = next(rgb)
        pygame.draw.line(display, (randint(0, col[0]), randint(0, col[1]), randint(0, col[2])), points[i - 1], points[i], randint(1, 100))

    points.append((randint(0, width), randint(0, height)))

    pygame.display.update()
    clock.tick(5)


pygame.quit()
