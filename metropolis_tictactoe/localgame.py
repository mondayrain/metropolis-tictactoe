'''
Class for object that runs a local game, varying by:
    - 1p or 2p
    - Level of difficulty
'''
import pygame
import time
import constants
from gameboard import GameBoard 
from movegenerator import MoveGenerator
from random import randint

class LocalGame:
    
    def __init__(self, mode, difficulty, screen, menu):
        """
        Constructor for a LocalGame class.

        Params:
        @mode = 1 or 2, repping either 1 or 2 players
        @difficulty = "Easy", Normal", or "Hard"; onlu ised if self.mode == 1.
        
        For the rest, see Game.py
        """
        self.mode = mode
        self.screen = screen
        self.current_player = None #x always goes first
        self.player = None    
        self.opponent = None
        self.menu = menu
        self.gameboard = GameBoard()
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
            
    def check_game_over(self):
        if ((self.gameboard.check_win(self.gameboard.x_list, constants.WIN_POSITION_LIST)) or (self.gameboard.check_win(self.gameboard.o_list, constants.WIN_POSITION_LIST))):
            return True
        else:
            return False

    def check_tie(self):
        if (len(self.gameboard.taken_positions_list) == 9) and (not (self.check_game_over())):
            return True
        else:
            return False
    
    def player_click(self, mouse_x, mouse_y):
        b_x = constants.BOARD_COORDINATES[0]
        b_y = constants.BOARD_COORDINATES[1]
        if b_x < mouse_x < (b_x + constants.TILE_DIMENSION):
            if (b_y < mouse_y < (b_y + constants.TILE_DIMENSION*3)) and ((((mouse_y - b_y) // 100)*3) not in self.gameboard.taken_positions_list):
                position = ((mouse_y - b_y) // 100)*3
                self.gameboard.update_player_list(self.current_player, position)
                self.switch_turns()
        elif b_x + constants.TILE_DIMENSION < mouse_x < (b_x + 2*constants.TILE_DIMENSION):
            if (b_y < mouse_y < (b_y + constants.TILE_DIMENSION*3)) and (((((mouse_y - b_y) // 100)*3+1) not in self.gameboard.taken_positions_list)):
                position = ((mouse_y - b_y) // 100)*3+1
                self.gameboard.update_player_list(self.current_player, position)
                self.switch_turns()       
        elif b_x + 2*constants.TILE_DIMENSION < mouse_x < (b_x + 3*constants.TILE_DIMENSION):
            if (b_y < mouse_y < (b_y + constants.TILE_DIMENSION*3)) and (((((mouse_y - b_y) // 100)*3+2) not in self.gameboard.taken_positions_list)):
                position = ((mouse_y - b_y) // 100)*3+2
                self.gameboard.update_player_list(self.current_player, position)
                self.switch_turns()
        elif (constants.GAME_BACK_ARROW_COOR[0] < mouse_x < constants.GAME_BACK_ARROW_COOR[0] + constants.BACK_ARROW.get_size()[0]):
            if (constants.GAME_BACK_ARROW_COOR[1] < mouse_y < constants.GAME_BACK_ARROW_COOR[1] + constants.BACK_ARROW.get_size()[1]):
                self.menu.current_state = 0
        if (constants.GAME_RESET_COOR[0] < mouse_x < constants.GAME_RESET_COOR[0] + constants.RESET.get_size()[0]):
            if (constants.GAME_RESET_COOR[1] < mouse_y < constants.GAME_RESET_COOR[1] + constants.RESET.get_size()[1]):
                self.reset_game()
            
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
        
    def draw_background(self):
        self.screen.blit(constants.BACKGROUND, (0,0))
        self.screen.blit(constants.HEADING, constants.HEADING_COORDINATES)
        self.screen.blit(constants.TITLE, constants.TITLE_COORDINATES)
        self.screen.blit(constants.BOARD_SURFACE, constants.BOARD_COORDINATES)
        
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
        
    def draw_marker_hover_helper(self, mouse_x, mouse_y):
        if (self.current_player == "x"):
            hover_marker = constants.HOVER_EX
        else:
            hover_marker = constants.HOVER_OH
        self.gameboard.draw_hover(mouse_x, mouse_y, hover_marker, self.screen, constants.BOARD_COORDINATES)
                
    def draw_markers(self):
        self.gameboard.draw_markers(self.screen, constants.BOARD_COORDINATES)
        
    def draw_buttons(self):
        self.screen.blit(constants.BACK_ARROW, constants.GAME_BACK_ARROW_COOR)
        self.screen.blit(constants.RESET, constants.GAME_RESET_COOR)
        
    def draw_buttons_hover(self, mouse_x, mouse_y):
        if (constants.GAME_BACK_ARROW_COOR[0] < mouse_x < constants.GAME_BACK_ARROW_COOR[0] + constants.BACK_ARROW.get_size()[0]):
            if (constants.GAME_BACK_ARROW_COOR[1] < mouse_y < constants.GAME_BACK_ARROW_COOR[1] + constants.BACK_ARROW.get_size()[1]):
                self.screen.blit(constants.BACK_ARROW_HOVER, constants.GAME_BACK_ARROW_COOR)
        if (constants.GAME_RESET_COOR[0] < mouse_x < constants.GAME_RESET_COOR[0] + constants.RESET.get_size()[0]):
            if (constants.GAME_RESET_COOR[1] < mouse_y < constants.GAME_RESET_COOR[1] + constants.RESET.get_size()[1]):
                self.screen.blit(constants.RESET_HOVER, constants.GAME_RESET_COOR)
    
    def draw_win (self, given_list):
        gset = set(given_list)
        for item in constants.WIN_POSITION_LIST:
            wset = set(item)
            intersection = wset.intersection(gset)
            if (len(intersection) == 3):
                if (self.current_player == "x"):
                    surface = constants.WINNING_EX
                else:
                    surface = constants.WINNING_OH
                for i in intersection:
                    
                    self.gameboard.draw_marker(self.current_player, i, self.screen, constants.BOARD_COORDINATES, surface)
            
    def reset_game(self):
        self.gameboard.x_list = []
        self.gameboard.o_list = []
        self.gameboard.taken_positions_list = []
        
    def switch_turns(self):
        if (self.current_player == self.player):
            self.current_player = self.opponent
        else:
            self.current_player = self.player 

