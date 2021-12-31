# 1- Import Packages
import pygame
import sys
from pygame.locals import *
from ball import Ball


# 2- Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 5
PATH_MUSIC = '../test/sounds/background.mp3'
N_BALLS = 3
# 3- Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4- Load assets: image(s), sound(s), etc.
pygame.mixer.music.load(PATH_MUSIC)
pygame.mixer.music.play(-1, 0.0)

# 5 - Initialize variables
balls_list = []
for ball in range(N_BALLS):
    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    balls_list.append(ball)

# 6 - Loop forever
while 1:
    # 7- Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8- Do any "per frame" actions
    for ball in balls_list:
        ball.update() # tell the Ball to update itself

    # 9- Clear the window
    window.fill(BLACK)

    # 10- Draw all window elements
    for ball in balls_list:
        ball.draw()

    # 11- Update the window
    pygame.display.update()

    # 12- Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
