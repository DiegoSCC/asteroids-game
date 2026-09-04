from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import pygame

from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")

    scr = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            # allows you to close the window and finish the process
            if event.type == pygame.QUIT:
                    return
            # this fills the screen with a black background, display.flip refreshes the screen
        scr.fill("black")
        player.draw(scr)
        player.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
