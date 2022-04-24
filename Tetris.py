# imports
import pygame
import random
from sys import exit
from pygame.locals import *
from Blocks import *
from controller import *
from colors import *

# Config pygame
pygame.init()
pygame.font.init() 
fontDefault = pygame.font.get_default_font()
font = pygame.font.SysFont(fontDefault, 25)
font2 = pygame.font.SysFont(fontDefault, 60)

# Config Window
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
MIN_WIDTH = 10
MIN_HEIGHT = 20
RECT_SIZE = 20
MARGIN_TOP = RECT_SIZE * 2
MARGIN_LEFT = RECT_SIZE * 2
SCREEN_WIDTH = MIN_WIDTH * RECT_SIZE
SCREEN_HEIGHT = MIN_HEIGHT * RECT_SIZE
DEFAULT_TICK = 20

fall_speed = 1
time = pygame.time
time_clock = pygame.time.Clock()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption("Tetris by KLT")

screen = pygame.Rect(MARGIN_TOP, MARGIN_LEFT, SCREEN_WIDTH, SCREEN_HEIGHT) # Main Screen

pos_x = (SCREEN_WIDTH / 2) + MARGIN_LEFT
pos_y = MARGIN_TOP
# Pieces
colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, CYAN]
squares_pieces_list = []
tetris_pieces_types = HERO, ORANGE_RICKY, BLUE_RICKY, CLEVELANDZ, RHODE_ISLAND_Z, TEWEE, SMASH_BOY
player_falls = True
player_fell = True
collided = False
play_game = True
score = 0

# Game Loop
while(True):
    # clear the window
    window.fill([100]*3)
    # set pygame time clock ticks
    time_clock.tick(DEFAULT_TICK)

    if player_fell and play_game:
        n_number = random.randint(0, 6)
        player = Block(tetris_pieces_types[n_number], pos_x, pos_y, RECT_SIZE, colors[n_number])
        player.Build()
        player_fell = False

    # get pygame events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # get keybords input
        if event.type == KEYDOWN:
            # if event.key == K_RETURN:
               
            if event.key == K_ESCAPE:
                if play_game:
                    play_game = False
                else:
                    player_fell = True
                    play_game = True
                    squares_pieces_list.clear()
            if (event.key == K_w or event.key == K_UP) and rotation_inspector(player, screen) and not blocksCollide(player, squares_pieces_list):
                player.Rotate()
    # get keybords continuous input
    keys_pressed = pygame.key.get_pressed()
    
    if (keys_pressed[K_a] or keys_pressed[K_LEFT])and move_inspector_left(player, screen) and not blocksCollide(player, squares_pieces_list):
        player.Move(-20, 0)
    elif (keys_pressed[K_d] or keys_pressed[K_RIGHT]) and move_inspector_right(player, screen) and not blocksCollide(player, squares_pieces_list):
        player.Move(20, 0)
    elif (keys_pressed[K_s] or keys_pressed[K_DOWN]) and move_inspector_bottom(player, screen) and not blocksCollide(player, squares_pieces_list):
        insignificant_height = player.anchor.y % 20
        if player.anchor.y != 0:
            adjust_height = 20 - insignificant_height
            player.Move(0, adjust_height)
        else:
            player.Move(0, 20)
        player_falls = False
    else:
        player_falls = True
    
    if blocksCollide(player, squares_pieces_list):
        collided = True   
        player_falls = False

    if player_falls and move_inspector_bottom(player, screen):
        if len(squares_pieces_list) > 0:
            if not blocksCollide(player, squares_pieces_list):
                player.Move(0, fall_speed)
        else:    
            player.Move(0, fall_speed)

    if play_game and (equals_bottom(player, screen) or collided):
        for i in blockdivisor(player):
            squares_pieces_list.append(i)
            if line_checker(squares_pieces_list):
                score += 10
        collided = False
        player_falls = False
        player_fell = True

    # draw text
    text_tutorials = font.render("Press W, A, D or S to Move", True, ([255]*3))
    text_tutorials2 = font.render("Press ESC to restart", True, ([255]*3))
    text_score = font.render(f"Score:{score}", True, ([255]*3))
    
    window.blit(text_tutorials, (SCREEN_WIDTH + MARGIN_LEFT * 1.3, MARGIN_TOP))
    window.blit(text_tutorials2, (SCREEN_WIDTH + MARGIN_LEFT * 1.3, MARGIN_TOP*2))
    window.blit(text_score, (SCREEN_WIDTH + MARGIN_LEFT * 1.3, MARGIN_TOP*3))
    # draw screen
    pygame.draw.rect(window, ([0]*3), screen)
    # draw all pieces
    player.Draw(window)

    for i in squares_pieces_list:
        pygame.draw.rect(window, ([255]*3), i)

    if not move_inspector_top(player, screen):
        for s in squares_pieces_list:
            if not screen.contains(s):
                play_game = False
                game_over = font2.render(f"Gamer Over", True, (255, 0, 0))
                window.blit(game_over, (pos_x, pos_y + MARGIN_TOP * 4))
    # update window
    pygame.display.update()
