import pygame # pyright: ignore[reportMissingImports]
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

score = 0

def destroy_asteroid():
    global score
    score += 100

def main():
    print("Starting Asteroids with pygame version:  2.6.1")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont(None, 36)  # or pygame.font.Font("path.ttf", 36)

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))  # top-left corner
        updatable.update(dt)
        for crash in asteroids:
            if crash.collides_with(player) == True:
                log_event("player_hit")
                log_event(f"{score}")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(crash) == True:
                    log_event("asteroid_shot")
                    destroy_asteroid()
                    shot.kill()
                    crash.split()
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
