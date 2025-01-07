import sys
import pygame
from plane import Hero
from plane import Soldier
from weapon import Bullet


size = width, height = 480, 700
is_running = True
is_pausing = False

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(r'Plane Wars')

    forms = pygame.display.set_mode(size)
    image = pygame.image.load(r'images\background\background.png')
    clock = pygame.time.Clock()

    hero = Hero()
    soldiers = []

    counter = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        while is_running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            forms.blit(image, (0, 0))

            hero.display(forms)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                hero.move_left()
            elif keys[pygame.K_RIGHT]:
                hero.move_right()
            else:
                pass

            hero.check_border()

            if counter % 100 == 0:
                soldiers.append(Soldier())

            for i in range(len(soldiers)):
                soldiers[i].display(forms)
                soldiers[i].move_down()

            counter += 1

            pygame.display.update()