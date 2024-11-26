import pygame
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, "Helpers"))
sys.path.insert(0, target_dir)
import vectors

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            raise SystemExit

        # Logic Updates Here

        # Changes background
        screen.fill("black")

        # Update Graphics here

        pygame.display.flip()
        clock.tick(60)
