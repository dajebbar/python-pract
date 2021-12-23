# 1 - Import packages
import pygame
import sys
import random
from pygame import key
from pygame.locals import *



# 2 - Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
# BASE_PATH = Path(__file__).resolve().parent
# Build a path to the file in the images folder
PATH_BALL = '../demo/images/ball.png'
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
PATH_TARGET = '../demo/images/target.jpg'
TARGET_X = 320
TARGET_Y = 220
TARGET_WIDTH_HEIGHT = 120
N_PIXEL_TO_MOVE = 5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()



# 4 - Load assets: image(s), sound(s),...
ball_img = pygame.image.load(PATH_BALL)
target_img = pygame.image.load(PATH_TARGET)

# 5 - Initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
# ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
target_rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6 - Loop Forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Quit and exit the App
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            if ball_rect.collidepoint(event.pos):
                ball_x = random.randrange(MAX_WIDTH)
                ball_y = random.randrange(MAX_HEIGHT)
                ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
        # One Click by click
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         ball_x  += N_PIXEL_TO_MOVE
        #     elif event.key == pygame.K_LEFT:
        #         ball_x -= N_PIXEL_TO_MOVE
        #     elif event.key == pygame.K_UP:
        #         ball_y -= N_PIXEL_TO_MOVE
        #     elif event.key == pygame.K_DOWN:
        #         ball_y += N_PIXEL_TO_MOVE

    
    # 8 - Do any "per frame" actions

    # Check for user pressing
    # Continus clicking
    key_press_tuple = pygame.key.get_pressed()
    if key_press_tuple[pygame.K_LEFT]: # moving left
        ball_x -= N_PIXEL_TO_MOVE
    if key_press_tuple[pygame.K_RIGHT]: # moving right
        ball_x += N_PIXEL_TO_MOVE
    if key_press_tuple[pygame.K_UP]: # moving top
        ball_y -= N_PIXEL_TO_MOVE
    if key_press_tuple[pygame.K_DOWN]: # moving botom
        ball_y += N_PIXEL_TO_MOVE

    # Check if the ball is colliding with the target
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ball_rect.colliderect(target_rect):
        print('Ball is touching the target')
        
    

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(target_img, (TARGET_X, TARGET_Y))
    # draw ball at random positions ball_x across (x) and ball_y down (y)
    window.blit(ball_img, (ball_x, ball_y))
    
    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)