import pygame
import vectors
import object

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
text_font = pygame.font.SysFont('Arial', 30)
G = 6.673430e-11


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def calc_tot_energy(p1, p2):
    kinetic = 0.5 * (p1.mass * p1.vel.magnitude() ** 2 + p2.mass * p2.vel.magnitude() ** 2)
    temp_pos = vectors.Vector2D(p1.pos.x, p1.pos.y)
    temp_pos.subtract(p2.pos)
    potential = G * p1.mass * p2.mass / (temp_pos.magnitude())
    return kinetic - potential


def calc_ang_momentum(p1, p2):
    ob1 = p1.mass*(p1.pos.x*p1.vel.y - p1.pos.y*p1.vel.x)
    ob2 = p2.mass*(p2.pos.x*p1.vel.y - p2.pos.y*p2.vel.y)
    return ob1 + ob2


planet1 = object.Object(vectors.Vector2D(400, 300), vectors.Vector2D(0, 0), 10e8, "light blue")
planet2 = object.Object(vectors.Vector2D(500, 300), vectors.Vector2D(0, -2.5), 10e6, "darkorchid1")

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            raise SystemExit

    # Logic Updates Here
    planet1.update(planet2)
    planet2.update(planet1)

    # Changes background
    screen.fill("black")

    # Update Graphics here
    planet1.draw(screen)
    planet2.draw(screen)

    draw_text("Total Angular Momentum: " + str(round(calc_ang_momentum(planet1, planet2), -8)), text_font, (255, 255, 255), 20, 500)
    draw_text("Total Energy: " + str(round(calc_tot_energy(planet1, planet2), -5)), text_font, (255, 255, 255), 20, 550)

    pygame.display.flip()
    clock.tick(60)
