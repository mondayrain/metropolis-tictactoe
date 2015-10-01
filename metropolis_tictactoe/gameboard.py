'''
Representation of the Tic Tac Toe game board with all the drawing functionality,
as well as lists of what positions each player has taken. 
'''
import constants

class GameBoard:

    TILE_DIMENSION = 100
    WIN_POSITION_LIST = WIN_POSITION_LIST = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
                                             (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    def __init__(self):
        self.x_list = []
        self.o_list = []
        self.taken_positions_list = []
        
    def draw_markers(self, screen, board_position):
        for item in self.x_list:
            self.draw_marker("x", item, screen, board_position, constants.EX)
        for item in self.o_list:
            self.draw_marker("o", item, screen, board_position, constants.OH)
        
    def draw_marker(self, player, position, screen, board_position, surface):
        if player == "x":
                marker_surface = surface
        else:
                marker_surface = surface
    
        board_x = board_position[0]
        board_y = board_position[1]
        h_displacement = (self.TILE_DIMENSION - marker_surface.get_size()[0])/2
        v_displacement = 14
        if (0 <= position <= 2):
            screen.blit(marker_surface, (board_x + position*self.TILE_DIMENSION + h_displacement, board_y + v_displacement))
        elif (3 <= position <= 5):
            screen.blit(marker_surface, (board_x + (position%3)*self.TILE_DIMENSION + h_displacement, board_y + self.TILE_DIMENSION + v_displacement))
        else:
            screen.blit(marker_surface, (board_x + (position%3)*self.TILE_DIMENSION + h_displacement, board_y + 2*self.TILE_DIMENSION + v_displacement))
            
    
            
    def draw_hover(self, mouse_x, mouse_y, hover_marker, screen, board_position):
        position = self.find_position(mouse_x, mouse_y, board_position)
        if (position not in self.taken_positions_list):
            if (position >= 0):
                h_displacement = (self.TILE_DIMENSION - hover_marker.get_size()[0])/2
                v_displacement = 14
                if (position%3) == 0:
                    screen.blit(hover_marker, (board_position[0] + h_displacement, board_position[1] + ((mouse_y - board_position[1]) // 100)*self.TILE_DIMENSION + v_displacement))
                elif (position%3) == 1:
                    screen.blit(hover_marker, (board_position[0] + self.TILE_DIMENSION + h_displacement, board_position[1] + ((mouse_y - board_position[1]) // 100)*self.TILE_DIMENSION + v_displacement))
                elif (position%3) == 2:
                    screen.blit(hover_marker, (board_position[0] + 2*self.TILE_DIMENSION + h_displacement, board_position[1] + ((mouse_y - board_position[1]) // 100)*self.TILE_DIMENSION + v_displacement))              
                
    #Update x or o list with new position chosen
    #if position is already taken, return false
    #otherwise, update list and return true.
    #@player_list = list being updated
    #@position = board position from 0-8
    def update_player_list (self, player, position):
        if position in self.taken_positions_list:
            return False
        else:
            if player == "x":
                self.x_list.append(position)
            else:
                self.o_list.append(position)
            self.update_taken_positions_list(position)
            return True
    
    #update taken positions list
    #assume that we have already checked if the position has previously been taken            
    def update_taken_positions_list (self, position):
        self.taken_positions_list.append(position)
        
    #Return true if player has won
    def check_win (self, player_list, win_list):
        if len(player_list) >= 3:
            for item in win_list:
                if item[0] in player_list and item[1] in player_list and item[2] in player_list: 
                    return True
        return False
    
    #Given coordinates, find whether or not they lie within a position coordinates
    #Return -1 if not
    def find_position(self, mouse_x, mouse_y, board_position):
        if (board_position[0] < mouse_x < (board_position[0] + self.TILE_DIMENSION)) and (board_position[1] < mouse_y < (board_position[1] + self.TILE_DIMENSION*3)):
                    position = ((mouse_y - board_position[1]) // 100)*3
                    return position
        if ((board_position[0] + self.TILE_DIMENSION < mouse_x < ((board_position[0] + 2*self.TILE_DIMENSION))) and (board_position[1] < mouse_y < (board_position[1] + self.TILE_DIMENSION*3))):
                    position = ((mouse_y - board_position[1]) // 100)*3+1
                    return position
        if ((board_position[0] + 2*self.TILE_DIMENSION < mouse_x < ((board_position[0] + 3*self.TILE_DIMENSION))) and (board_position[1] < mouse_y < (board_position[1] + self.TILE_DIMENSION*3))):
                    position = ((mouse_y - board_position[1]) // 100)*3+2
                    return position
        else:
            return -1
    
