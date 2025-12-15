import pygame # pyright: ignore[reportMissingImports]
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from circleshape import CircleShape
from player import Player

def main():
    print("Starting Asteroids with pygame version:  2.6.1")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
    pygame.quit()

if __name__ == "__main__":
    main()
