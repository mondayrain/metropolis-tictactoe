import pygame
import constants
from  localgame import LocalGame
from menu import Menu
from onlinegame import OnlineHostGame, OnlineClientGame

def main(args=None):
    """ SET UP """
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
    menu = Menu(screen)

    #Initialize Music
    current_track = menu.track
    pygame.mixer.init(44100)
    if (pygame.mixer.get_init()):
        pygame.mixer.music.load(current_track)
        pygame.mixer.music.play(-1)

    """ MAIN EVENT LOOP """ 
    while (menu.current_state >= 0):    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                menu.current_state = -1
            
        if (menu.current_state == Menu.STATE_MAIN):
            menu.run_menu_page(screen)
        
        elif (menu.current_state == Menu.STATE_ONE_PLAYER):
            game = LocalGame(screen, menu, 1)
            game.run_game()
        
        elif (menu.current_state == Menu.STATE_TWO_PLAYER):
            game = LocalGame(screen, menu, 2)
            game.run_game()

        elif (menu.current_state == Menu.STATE_ONLINE):
            # Should determine whether or not there is already a host
            # on the LAN. If not, player becomes host and waits for someone to join.
            # Otherwise, player is client and joins host game.
            IP = detect_host_ip()
            if IP:
               game = OnlineClientGame() 
            else:
               game = OnlineHostGame()
            game.run_game()
        
        elif (menu.current_state == Menu.STATE_SETTINGS):
            menu.run_settings_page(screen)

        # This should never happen; if so, we stay in the menu
        else:
            menu.current_state = Menu.STATE_MAIN

if __name__ == "__main__" :
    main()
