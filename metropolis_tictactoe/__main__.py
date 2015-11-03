import pygame
import constants
from localgame import LocalGame
from menu import Menu
from time import sleep
import socket
#from onlinegame import OnlineHostGame, OnlineClientGame

HOST = 0
CLIENT = 1
HOST_WAIT_TIME = 20
CLIENT_WAIT_TIME = 10
PORT = 63800 # Default port
             # TODO: Let user choose the port in the settings page

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

        # We put logic for updating the waiting message out here,
        # so that the user can still exit the game if they want.
        if menu.waiting:
            if menu.waiting_time > 0:
                menu.waiting_time -= 1
            elif menu.waiting_time <= 0 and online_role == CLIENT:
                menu.waiting_time = HOST_WAIT_TIME
                online_role = HOST
            else:
                # Tried both being and finding a host; both failed.
                # Terminate trying to start an online game.
                menu.waiting = False
                menu.waiting_time = CLIENT_WAIT_TIME
                menu.current_state = Menu.STATE_MAIN

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

            # Online play just clicked; initialize all variables we need to use
            # to start a new online game.
            if not menu.waiting:
                menu.waiting = True
                IP = None             # IP address of client/host to connect to
                playersocket = None         # UDP socket to use
                online_role = CLIENT  # Player always tries to find a game first
                                      # before becoming a host

            # Other wise, we continue what we were doing before
            else:
                # We're currently a client
                if online_role == CLIENT:
                    # Set up socket if and send out broadcast message to servers
                    # if we haven't already.
                    if not playersocket:
                         playersocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                         playersocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                         playersocket.setblocking(0)

                         try:
                             playersocket.sendto("METROPOLISTICTACTOE", ('<broadcast>', PORT))
                         except socket.error:
                             menu.draw_message(screen, "Socket error: couldn't connet to a host game. Try again later.")
                             menu.waiting = False  
                             menu.current_state = Menu.STATE_MAIN
                    # See if any hosts have answered us 
                    else:
                         try:
                             data, address = playersocket.recvfrom(2048)
                             # We found a host!
                             if "METROPOLISTICTACTOE" in data:
                                  # TODO: Create client game 
                                  # TODO: Run client game
                                  pass
                         except socket.error:
                             pass
                # We're currently a host
                else:
                    # Set up socket if it hasn't already been set up.
                    if not playersocket:
                         playersocket = socket.socket((socket.AF_INET, socket.SOCK_DGRAM))
                         playersocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
                         playersocket.setblocking(0)
                         playersocket.bind(('', PORT))
                    # See if any clients have contacted us
                    else:
                        try:                 
                            data, address = playersocket.recvfrom(2048)
                            if "METROPOLISTICTACTOE" in data:
                                # TODO: send back a reply!
                                # TODO: create host game
                                # TODO: run host game
                                pass
                        except socket.error:
                            pass

                menu.draw_page(screen)
                menu.draw_message(screen, "Searching for a game to join: %d" % menu.waiting_time)
                pygame.display.flip()
        
        elif (menu.current_state == Menu.STATE_SETTINGS):
            menu.run_settings_page(screen)

        # This should never happen; if so, we stay in the menu
        else:
            menu.current_state = Menu.STATE_MAIN

if __name__ == "__main__" :
    main()
