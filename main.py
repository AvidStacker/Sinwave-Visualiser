import math
import pygame

WIDTH = 800
HEIGHT = 800

FPS = 60

def map(value, start1, stop1, start2, stop2, clamp=False):
    numerator = value - start1
    denominator = stop1 - start1
    mapped_val = (numerator / denominator) * (stop2 - start2) + start2
    
    # Clamp the value if specified
    if clamp:
        if mapped_val < start2:
            return start2
        elif mapped_val > stop2:
            return stop2
    
    return mapped_val

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    angle = 0
    
    color = "black"

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        rect_width = 24
        offset = 0
        # Rita rektangeln
        for x in range(0, WIDTH, rect_width):
            sin_val = math.sin(angle + offset)
            # Mappa för att gå neråt (0 till -100) och sedan uppåt (0 till 100)
            oscillation = map(sin_val, -1, 1, 0, 100)  # Från 0 till 100
            rect_height = oscillation  # Höjden av rektangeln

            # Beräkna y-positionen så att rektangeln växer uppåt och nedåt
            rect_y = (HEIGHT / 2) - (rect_height / 2)

            rectangle = pygame.Rect(x, rect_y, rect_width - 2, rect_height)
            
            pygame.draw.rect(screen, color, rectangle)
            
            offset += 0.05

        angle += 0.1  # Öka vinkeln för att få oscillerande rörelse

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
