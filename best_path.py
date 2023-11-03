import pygame

# Setting the Screen Height
width, height = 800, 800


def screenSize(width, height):
    screen = pygame.display.set_mode((width, height))
    return screen


screen = screenSize(width, height)


def drawGrid(gridSize, gridColor):
    for x in range(0, width, gridSize):
        pygame.draw.line(screen, gridColor, (x, 0), (x, height))
    for y in range(0, height, gridSize):
        pygame.draw.line(screen, gridColor, (0, y), (width, y))


def runGame():
    pygame.init()

    backgroundColor = (255, 255, 255)
    pygame.display.set_caption("Best Path")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(backgroundColor)
        drawGrid(50, (200, 200, 200))
        pygame.display.flip()


runGame()
pygame.quit()
