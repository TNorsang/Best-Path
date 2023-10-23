import pygame


# Setting the Screen Height


def screenSize(width, height):
    screen = pygame.display.set_mode((width, height))
    return screen


screen = screenSize(800, 800)


def runGame():
    pygame.init()

    backgroundColor = (255, 255, 255)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == ßßpygame.QUIT:
                running = False
        screen.fill(backgroundColor)
        pygame.display.flip()


runGame()
pygame.quit()
