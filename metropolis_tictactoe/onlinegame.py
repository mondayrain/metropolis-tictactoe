'''
Classes and functionality for running a game on a LAN on a server-client model.

OnlineHostGame represents the host/server.
OnlineClientGame represents the client.
'''

import pygame
import socket
import constants
from game import Game


class OnlineHostGame(Game):
    def __init__(self, screen, menu, self_ip, client_ip, port):
        super(OnlineHostGame, self).__init__(screen, menu)
        self.ip_addr = self_ip
        self.client_addr = client_ip
        self.port = port
        self.socket_status = self.SOCKET_OK
        self.client_move = None

    def run_game(self):
        # Create IPv4 TCP socket
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            self.socket_status = self.SOCKET_ERROR

        # Set low timeout value to detect client dropping connection
        server_socket.settimeout(10.0)

        # Bind to socket
        try:
            server_socket.bind(('', self.port))
        except socket.error:
            self.socket_status = self.SOCKET_ERROR

        # If we get a socket error, go back to main menu
        if not self.socket_status == self.SOCKET_OK:
            self.draw_socket_failure()
            time.sleep(5)
            self.menu.current_state = 0
    
        ''' Game Loop '''
        # Host always goes first
        self.player = 'x'
        self.current_player = 'x'
        self.opponent = 'o'

        while self.socket_status == self.SOCKET_OK:
            while not self.check_game_over() and not self.check_tie() and (self.menu.current_state != Menu.STATE_MAIN):
		# try-block for catching a dropped socket error
		try:
		    # Event Processing
		    # Host always goes first
		    mouse_click = (0,0)
		    self.mouse_position = pygame.mouse.get_pos()
		    for event in pygame.event.get():
			if event.type == pygame.QUIT:
			    self.menu.current_state = -1
			    return
			if event.type == pygame.MOUSEBUTTONUP:
			    mouse_click = self.mouse_position

		    # Logic
		    if (self.current_player == self.player):
			self.handle_player_click(mouse_click[0], mouse_click[1])
			# Draw change
			draw_game()
			time.sleep(2)
			# Send off change to client and switch turns
			self.construct_state()
			#TODO: send off state to client
			self.switch_turns()

		    # Client/server interaction 
		    #TODO: listen for response
                    server_socket.listen(1)
		    self.unpack_move()
		    draw_game()
		except SocketError, e:
		    self.socket_status = self.SOCKET_FAILED

	    # Once we leave the game loop, check if we need to display:
	    # - win/loss
	    # - tie
	    # - connection error screen
	    if self.check_game_over() or self.check_tie():
		self.draw_game()
                time.sleep(5)
                self.reset_game()

	    elif self.socket_status == self.SOCKET_FAILED:
		self.draw_socket_failure()

	    else:
		# player simply left the game
                # menu has already been set; we get out of here
		# close the socket
                server_socket.close()
                self.socket_status = self.SOCKET_FAILED 

    def unpack_move(self):
        pass
        
    def construct_state(self):
        pass

class OnlineClientGame(Game):
    def __init__(self, screen, menu):
        super(OnlineClientGame, self).__init__(screen, menu, self_ip, host_ip, port)
        self.ip_addr = self_ip
        self.host_addr = host_ip
        self.port = port
        self.socket_status = self.SOCKET_OK

