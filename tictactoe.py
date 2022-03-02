#!/usr/bin/env python

import pygame, sys
import numpy as np
import time

pygame.init()
#----------
#CONSTANCES
#----------

#screen setup:
WIDTH = 600
HEIGHT = WIDTH

#grid setup:
BOARD_ROWS = 3
BOARD_COLS = 3
#screensetup2:
SQUARE_SIZE = WIDTH//BOARD_COLS
LINE_WIDTH = SQUARE_SIZE//13 # or ONLY 15
#colors:
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
#circle constances:
CIRCLE_COLOR = (239, 231, 200)
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = SQUARE_SIZE//13 #or ONLY 15
#cross constances:
CROSS_WIDTH = SQUARE_SIZE//8 #or ONLY 8
SPACE = SQUARE_SIZE//4
CROSS_COLOR = ( 66, 66, 66 )

#screen init:
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

#rest
alwaystrue = True
game_over = False

#---------
#FUNKTIONS
#---------

def delay():
    time.sleep(1)

def draw_lines():
   #1 horizontal line:
    pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
   #2 horizontal line:
    pygame.draw.line(screen, LINE_COLOR, (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)
   #1 vertial line:
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
   # 2 vertial line:
    pygame.draw.line(screen, LINE_COLOR, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
           if board[row][col] == 1:
               pygame.draw.circle(screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )

           elif board[row][col] == 2:
               pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
               pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

def alles_weg():
    for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
           board[row][col] == 0
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row] [col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
           if board[row][col] == 0:
               return False
    return True

def check_win(player):
    #vertical win check:
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    #horizontal win check:
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    #asc diagonal win check:
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #desc diagonal winning check:
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )


def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH )


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:                   
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH )


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH )


def restart():
    screen.fill( BG_COLOR )
    draw_lines()
    game_over = False
    player = 1

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] == 0


#draw the grid
draw_lines()

player = 1
font = pygame.font.Font(None, 48)
text = font.render("Press Space for restart", True, (0, 0, 0))


#--------
#MAINLOOP:
#--------

while alwaystrue == True:
    #press space schriftzug                                             
    screen.blit(text,                                                   
            (300 - text.get_width() // 2, 15 - text.get_height() // 2)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
                draw_figures()



            #if is_board_full():
             #   draw_figures()
              #  delay()
               # game_over = False
                #board = np.zeros((BOARD_ROWS, BOARD_COLS))
                #restart()
                #print(board)


        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_SPACE:
                sys.exit()
                pygame.QUIT()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = False
                board = np.zeros((BOARD_ROWS, BOARD_COLS))
                restart()

        else:
            continue
                
    pygame.display.update()