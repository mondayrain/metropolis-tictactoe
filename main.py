'''
Main file for running program
Note that Menu's current_state controls what is currently happening;
0 = main menu
1 = 1P game
2 = 2P game
3 = Online game
4 = Settings page
'''
import pygame
import constants
import LocalGame
import Menu

'''''''''
SET-UP
'''''''''
#Set-up screen
pygame.init()
pygame.font.init()
pygame.display.init()
SIZE = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("METROPOLIS Tic Tac Toe")
constants.BOARD_SURFACE.convert_alpha()
constants.BOARD_SURFACE.set_alpha(37)

#Run program
current_state = 0
menu = Menu.Menu(screen)

#Initialize Music
current_track = menu.track
pygame.mixer.init(44100)
if (pygame.mixer.get_init()):
    pygame.mixer.music.load(current_track)
    pygame.mixer.music.play(-1)


while (menu.current_state >= 0):    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            menu.current_state = -1
            
    localGame = LocalGame.LocalGame(1, menu.diff, screen, menu)
    
    if (menu.current_state == 0):
        menu.run_menu_page(screen)
        
    if (menu.current_state == 1):
        localGame.mode = 1
        localGame.run_game()
        
    if (menu.current_state == 2):
        localGame.mode = 2
        localGame.run_game()
        
    if (menu.current_state == 4):
        menu.run_settings_page(screen)
        