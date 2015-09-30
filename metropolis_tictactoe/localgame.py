'''
Class for object that runs a local game, varying by:
    - 1p or 2p
    - Level of difficulty
'''
import pygame
import time
import constants
from game import Game
from gameboard import GameBoard 
from movegenerator import MoveGenerator
from random import randint


class LocalGame(Game):
    
    def __init__(self, screen, menu, mode, difficulty):
        """
        Constructor for a LocalGame class.

        Params:
        @mode = 1 or 2, repping either 1 or 2 players
        @difficulty = "Easy", Normal", or "Hard"; only used if self.mode == 1.
       
         
        For the rest, see Game.py
        """
        super(LocalGame, self).__init__(screen, menu)
        self.mode = mode
        self.AI = MoveGenerator(difficulty)
    
    def run_game(self):
        clock = pygame.time.Clock()
        #Determine whether AI or player goes first
        self.determine_turns()
        '''Game Loop'''
        while (not (self.check_game_over() or self.check_tie()) and (self.menu.current_state != 0)):
            #Event Processing
            mouse_click = (0,0)
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.menu.current_state = -1
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click = mouse_position
            #Logic
            if (self.mode == 1):
                if (self.current_player == self.player):
                    self.player_click(mouse_click[0], mouse_click[1])
                else:
                    self.opponent_move()
            elif (self.mode == 2):
                try:
                    mouse_x = mouse_click[0]
                    mouse_y = mouse_click[1]
                    self.player_click(mouse_x, mouse_y)
                except:
                    pass
                    
            #Drawing
            self.draw_background()
            self.draw_buttons()
            self.draw_buttons_hover(mouse_position[0], mouse_position[1])
            self.draw_marker_hover(mouse_position[0], mouse_position[1])
            self.gameboard.draw_markers(self.screen, constants.BOARD_COORDINATES)
            if (self.check_game_over()):
                self.switch_turns() #Turn is switched after move, so switch back to draw winner correctly
                if (self.current_player == "x"): 
                    l = self.gameboard.x_list
                else:
                    l = self.gameboard.o_list
                self.draw_win(l)
                
            pygame.display.flip()
            
            #If the game is over, pause for a moment to let player see that game is over
            if (self.check_game_over() or self.check_tie()):
                time.sleep(1)
            clock.tick(60)
    

    def determine_turns(self):
        """
\       Determine which player is 'x' and which player is 'o'.
        'x' always goes first.
        """
        num = randint(1,10)
        if (num%2 == 0):
            self.player = "x"
            self.opponent = "o"
            self.current_player = self.player
        else:
            self.player = "o"
            self.opponent = "x"
            self.current_player = self.opponent
             
    def opponent_move(self):
        if self.current_player == "x":
            AI_list = self.gameboard.x_list
            player_list = self.gameboard.o_list
        else:
            AI_list = self.gameboard.o_list
            player_list = self.gameboard.x_list
            
        time.sleep(0.2)
        pc_move = self.AI.generate_move(AI_list, player_list, self.gameboard.taken_positions_list)
        self.gameboard.update_player_list(self.current_player, pc_move)
        self.switch_turns()
         
    def draw_marker_hover(self, mouse_x, mouse_y):
        """
        Draw transparent hover icon when player mouse overs.
        If local-player, mode 1 means 1-player; if online game,
        mode 1 means it
        """
        if (self.mode == 1):
            if (self.current_player == self.player):
                    self.draw_marker_hover_helper(mouse_x, mouse_y)
        else:
            self.draw_marker_hover_helper(mouse_x, mouse_y)
        
