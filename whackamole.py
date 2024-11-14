import pygame
import random

# hello
def draw_lines(screen):
    for i in range(1, 16):
        pygame.draw.line(
            screen,
            "black",
            (0, i * 32),
            (640, i * 32),
        )
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            "black",
            (i * 32, 0),
            (i * 32, 512)
        )
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        # screen.fill("light green")
        # screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        # draw_lines(screen)
        # pygame.display.flip()
        pos_row = 0
        pos_col = 0
        current_row = 0
        current_col = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    print(row,col)
                    if row == current_row and col == current_col:
                        current_row = random.randrange(0, 16)
                        current_col = random.randrange(0, 20)
                        pos_row = current_row * 32
                        pos_col = current_col * 32

            screen.fill("light green")
            draw_lines(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(pos_col, pos_row)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
