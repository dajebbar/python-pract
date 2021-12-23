# 1- Import Packages
import pygame
import sys
import random
from pygame.locals import *


# 2- Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 5
PATH_IMG = '../demo/images/ball.png'
# 3- Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4- Load assets: image(s), sound(s), etc.
ball_img = pygame.image.load(PATH_IMG)

# 5- Initialize variables
ball_rect = ball_img.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ball_rect.width
MAX_HEIGHT = WINDOW_HEIGHT - ball_rect.height
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_PER_FRAME
y_speed = N_PIXELS_PER_FRAME
# 6- Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close btn? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8- Do any "per frame" actions
    if (ball_rect.left < 0) or (ball_rect.right >= WINDOW_WIDTH ):
        x_speed = -x_speed
    if (ball_rect.top < 0) or (ball_rect.bottom >= WINDOW_HEIGHT):
        y_speed = -y_speed
    
    ball_rect.left += x_speed
    ball_rect.top += y_speed

    # 9- Clear the window
    window.fill(BLACK)

    # 10- Draw all window elements
    window.blit(ball_img, ball_rect)

    # 11- Update the window
    pygame.display.update()

    # 12- Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
