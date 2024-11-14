import pygame


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            clock.tick(60)
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    "black",
                    (0, i * 32),
                    (640, i * 32),
                )
            for i in range(1, 24):
                pygame.draw.line(
                    screen,
                    "black",
                    (i * 32, 0),
                    (i * 32, 512)
                )
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
