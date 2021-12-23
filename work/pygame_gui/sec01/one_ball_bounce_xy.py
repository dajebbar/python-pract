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
PATH_BALL = '../demo/images/ball.png'
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
N_PIXEL_TO_MOVE = 5
# 3- Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4- Load assets: image(s), sound(s), etc.
ball_img = pygame.image.load(PATH_BALL)

# 5- Initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
x_speed = N_PIXEL_TO_MOVE
y_speed = N_PIXEL_TO_MOVE


# 6- Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close btn? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8- Do any "per frame" actions
    if (ball_x < 0) or (ball_x >= MAX_WIDTH):
        x_speed = -x_speed # reverse x direction
    if (ball_y < 0) or (ball_y >= MAX_HEIGHT):
        y_speed = -y_speed # reverse y direction
    # Update the ball's location, using the speed in two directions
    ball_x += x_speed
    ball_y += y_speed

    # 9- Clear the window
    window.fill(BLACK)

    # 10- Draw all window elements
    window.blit(ball_img, (ball_x, ball_y))

    # 11- Update the window
    pygame.display.update()

    # 12- Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


# # 1 - Import packages
# import pygame
# from pygame.locals import *
# import sys
# import random

# # 2 - Define constants
# BLACK = (0, 0, 0)
# WINDOW_WIDTH = 640
# WINDOW_HEIGHT = 480
# FRAMES_PER_SECOND = 30
# BALL_WIDTH_HEIGHT = 100
# N_PIXELS_PER_FRAME = 3

# # 3 - Initialize the world
# pygame.init()
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# clock = pygame.time.Clock()
 
# # 4 - Load assets: image(s), sound(s),  etc.
# ballImage = pygame.image.load('../demo/images/ball.png')

# # 5 - Initialize variables
# MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
# MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
# ballX = random.randrange(MAX_WIDTH)
# ballY = random.randrange(MAX_HEIGHT)
# xSpeed = N_PIXELS_PER_FRAME
# ySpeed = N_PIXELS_PER_FRAME
 
# # 6 - Loop forever
# while True:

#     # 7 - Check for and handle events
#     for event in pygame.event.get():
#         # Clicked the close button? Quit pygame and end the program  
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
    
#     # 8 - Do any "per frame" actions
#     if (ballX < 0) or (ballX >= MAX_WIDTH):
#         xSpeed = -xSpeed  # reverse X direction

#     if (ballY < 0) or (ballY >= MAX_HEIGHT):
#         ySpeed = -ySpeed  # reverse Y direction

#     # Update the ball's location, using the speed in two directions
#     ballX = ballX + xSpeed
#     ballY = ballY + ySpeed

#     # 9 - Clear the window before drawing it again
#     window.fill(BLACK)
    
#     # 10 - Draw the window elements
#     window.blit(ballImage, (ballX, ballY))

#     # 11 - Update the window
#     pygame.display.update()

#     # 12 - Slow things down a bit
#     clock.tick(FRAMES_PER_SECOND)  # make pygame wait