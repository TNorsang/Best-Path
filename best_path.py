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
    gridSize = 50
    backgroundColor = (255, 255, 255)
    blue = (0, 141, 207)
    pygame.display.set_caption("Best Path")
    running = True
    count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    # Fill the screen with blue upon left button click
                    x, y = event.pos
                    i = x // gridSize
                    j = x // gridSize

                    count += 1
                    print(f"Button Clicked {count}, x = {x} y = {y}")

        # Fill the screen with the background color
        screen.fill(backgroundColor)
        drawGrid(gridSize, (200, 200, 200))
        pygame.display.flip()


runGame()
pygame.quit()
