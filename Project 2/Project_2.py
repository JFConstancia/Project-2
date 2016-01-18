import time
from threading import Thread
import os, pygame
import time

pygame.init()
size = width, height = 1700, 1080
black = 0, 0, 0
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10

board = pygame.image.load("Content/Board.jpg")
play = pygame.image.load("Content/Play.png").convert()
play_hover = pygame.image.load("Content/Play_hover.png").convert()
exit = pygame.image.load("Content/Quit.png").convert()
exit_hover = pygame.image.load("Content/Quit_hover.png").convert()
play_r = play.get_rect()
play_r.x, play_r.y = (705, 360)
exit_r = exit.get_rect()
exit_r.x, exit_r.y = (705, 460)
def Main():
  play_r = play.get_rect()
  play_r.x, play_r.y = (705, 360)
  start = time.time()
  playing = False
  currentscreen = 0
  Hover_play_r = False
  Hover_exit_r = False
  while True:    
    pygame.event.pump() 
    # 0 = First Menu
    # 1 = After menu > amount players
    # 2 = Board game
    # 3 = Pause menu
    if playing == False:
        if Hover_play_r == True:
            screen.blit(play_hover, (705,360))
            currentscreen = 0
        elif Hover_exit_r == True:
            screen.blit(exit_hover, (705, 460))
            currentscreen = 0
        else:
            screen.fill(black)
            screen.blit(play, (705,360))
            screen.blit(exit, (705,460))
            currentscreen = 0
    for event in pygame.event.get():
        if play_r.collidepoint(pygame.mouse.get_pos()):
            Hover_play_r = True
        else:
            Hover_play_r = False
        if exit_r.collidepoint(pygame.mouse.get_pos()):
            Hover_exit_r = True
        else:
            Hover_exit_r = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            print(pos_x)
            print(pos_y)
            if (pos_x > 704) and (pos_x < 960) and (pos_y > 359) and (pos_y < 406):
                print("PLAY")
                playing = True
                if playing == True and currentscreen == 0:
                    screen.fill(black)
                    pygame.font.init()
                    myfont = pygame.font.SysFont("monospace", 30)
                    label = myfont.render("Choose amount of players.", 1, (255,255,255))
                    screen.blit(label, (425, 200))
                    currentscreen = 1
            elif (pos_x > 704) and (pos_x < 960) and (pos_y > 459) and (pos_y < 506):
                if currentscreen == 0:
                    pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if currentscreen == 1:
                    screen.blit(board, (0,0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing == False
                screen.fill(black)
                screen.blit(play, (705,360))
                screen.blit(quit, (705,460))
                currentscreen = 3

        #elif event.type == pygame.MOUSEMOTION:
        #    print("mouse at (%d, %d)" % event.pos)
    
    pygame.display.flip()
    time.sleep(0.01)
    
Main()