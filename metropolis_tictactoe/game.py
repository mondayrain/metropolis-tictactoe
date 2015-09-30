import pygame
import constants
from gameboard import GameBoard

class Game:
    """
    Half-abstract class for a Tic Tac Toe Game. Provides base/common functionality
    for detecting which tile has been clicked, drawing buttons, detecting wins,
    switching turns, etc. Also declares methods that must be implemented by
    subclassing Games. 
    """

    def __init__(self, screen, menu):
        """
        Constructor for the Game class.
        
        Params:
            @screen = pygame.Surface to draw to.
            @menu = instance of the Menu() object used in main. Used to determine whether
                    or not the player has quit the game, so we can return to main menu screen.
            @gameboard = instance of a GameBoard().
            @player = the player symbol; either 'x' or 'o'.
            @opponent = the opponent symbol; either 'x' or 'o' 
            @current_player = player who's turn it currently is.
        """
        self.screen = screen
        self.menu = menu
        self.gameboard = GameBoard()
        self.player = None
        self.current_player = None
        self.opponent = None

    def determine_turns(self):
        """
        Method called at the beginning of a Game to determine who will play as 'x' and
        who will play as 'o'. Must be implemented by a subclass of Game.
        """
        raise NotImplementedError("Subclass of Game must implement determine_turns")

    def opponent_move(self):
        """
        Defines functionality during the opponent's turn. Must be implemented by a subclass of Game.
        """
        raise NotImplementedError("Subclass of Game must implement opponent_move")

    def draw_marker_hover(self):
        """
        Draw transparent hover icon when player mouses over a tile.
        Should use draw_marker_hover_helper.
        Must be implemented by a subclass of Game.
        """
        raise NotImplementedError("Subclass of Game must implement draw_marker_hover")

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

    def draw_background(self):
        self.screen.blit(constants.BACKGROUND, (0,0))
        self.screen.blit(constants.HEADING, constants.HEADING_COORDINATES)
        self.screen.blit(constants.TITLE, constants.TITLE_COORDINATES)
        self.screen.blit(constants.BOARD_SURFACE, constants.BOARD_COORDINATES)


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
        """
        Used to highlight the winning markers. To be called after check_game_over()
        has confirmed that there is a winner; given_list is the list of
        markers for the winning player.
        """
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

    def player_click(self, mouse_x, mouse_y):
        """
        Functionality for responding to the active players' clicks during their turn.
        
        Side effects:
        - If an invalid tile is clicked, nothing will happen.
        - If a valid tile is clicked, the player's marker list will be updated and
          turns will be switched.
        - If the exit button is clicked, menu's state will be switched to 0.
        - If the reset button is clicked, reset_game() will be called.
        """
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

