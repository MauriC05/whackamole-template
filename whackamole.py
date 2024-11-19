import pygame
import random


def main():
    pygame.display.set_caption("Whackamole")
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill((52, 235, 232))
        x = 0
        while x != 640:
            x += 32
            pygame.draw.line(screen, "orange", (x, 0), (x, 512))
        y = 0
        while y != 512:
            y += 32
            pygame.draw.line(screen, "orange", (0, y), (640, y))
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        pygame.display.flip()
        while running:
            screen.fill((52, 235, 232))
            x = 0
            while x != 640:
                x += 32
                pygame.draw.line(screen, "orange", (x, 0), (x, 512))
            y = 0
            while y != 512:
                y += 32
                pygame.draw.line(screen, "orange", (0, y), (640, y))
            # screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            # pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                # screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
                # pygame.display.flip()
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x <= 32 and y <= 32:
                        screen.fill((52, 235, 232))
                        x = 0
                        while x != 640:
                            x += 32
                            pygame.draw.line(screen, "orange", (x, 0), (x, 512))
                        y = 0
                        while y != 512:
                            y += 32
                            pygame.draw.line(screen, "orange", (0, y), (640, y))
                        m = 32 * (random.randrange(0, 20))
                        n = 32 * (random.randrange(0, 16))
                        screen.blit(mole_image, mole_image.get_rect(topleft = (m , n)))
                        pygame.display.flip()
                    if m <= x <= m + 32 and n <= y <= n + 32:
                        screen.fill((52, 235, 232))
                        x = 0
                        while x != 640:
                            x += 32
                            pygame.draw.line(screen, "orange", (x, 0), (x, 512))
                        y = 0
                        while y != 512:
                            y += 32
                            pygame.draw.line(screen, "orange", (0, y), (640, y))
                        m = 32 * (random.randrange(0, 20))
                        n = 32 * (random.randrange(0, 16))
                        print(m, n)
                    screen.blit(mole_image, mole_image.get_rect(topleft=(m, n)))
                    pygame.display.flip()





    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
