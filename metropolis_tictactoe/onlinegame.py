'''
Classes and functionality for running a game on a LAN on a server-client model.
GameBridge acts as the intermediary between the server and client, providing
functionality for detecting hosts and clients.

OnlineHostGame represents the host/server.
 OnlineClientGame represents the client.
'''

import pygame
import constants
from game import Game

`
class OnlineHostGame(Game):
    def __init__(self, screen, menu):
        super(OnlineHostGame, self).__init__(screen, menu)


class OnlineClientGame(Game):
    def __init__(self, screen, menu):
        super(OnlineClientGame, self).__init__(screen, menu)

 
class GameBridge(object):
    pass
