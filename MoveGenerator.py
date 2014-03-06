'''
The AI that generates the computer's next move, with the AI strategy dependent on whether
the computer's level has been set at "easy", "normal", "hard", or "impossible"

Strategies: 
(ideas taken from http://frankanya.wordpress.com/2013/04/16/non-recursive-tic-tac-toe-ai-algorithm/)
1) Easy: Randomly choose a number from 0-8
2) Normal: Implements blocking and ability to recognize a next-move win
3) Hard: Minimax algorithm
'''
from random import randint
from random import choice

class MoveGenerator:
    
    WIN_POSITION_LIST = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), 
                     (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    FIRST_MOVES = [0, 2, 4, 6, 8]
    
    CORNERS = [0,2,6,8]

    def __init__(self, difficulty):
        self.diff = difficulty
    
    #Returns a number indicating the position of the move AI will make,
    #depending on level of difficulty
    def generate_move(self, AI_list, player_list, taken_list):
        if (self.diff == "Easy"):
            return (self.generate_move_easy(taken_list))
        elif (self.diff == "Normal"):
            return (self.generate_move_normal(AI_list, player_list, taken_list))
        else:
            return (self.generate_move_hard(AI_list, player_list, taken_list))
        
    #Randomly choose any free position on the board
    def generate_move_easy(self, taken_list):
        move = randint(0,8)
        while (move in taken_list):
            move = randint(0,8)
        return move
    
    #If AI can win, choose that spot.
    #If player could win next turn, block player.
    #Otherwise, choose random open spot
    def generate_move_normal(self, AI_list, player_list, taken_list):
        AI_win = self.can_win(AI_list, taken_list)
        if (AI_win >= 0):
            return AI_win
        elif (self.can_win(player_list, taken_list) >= 0):
            return (self.can_win(player_list, taken_list))
        else:
            return self.generate_move_easy(taken_list)   
        
    #Minimax algorithm, with strategic checks prior to speed up decision-making process
    def generate_move_hard(self, AI_list, player_list, taken_list):
        #If going first, choose a "safe" position
        if (len(taken_list) == 0):
            return choice(self.FIRST_MOVES)
        
        #If other player went first and...
        if ((len(taken_list) == 1) and (len(player_list) == 1)):
            #Took a corner, choose middle
            if (player_list[0] in self.CORNERS):
                return 4
            #Took the middle, choose a corner
            if (player_list[0] == 4):
                return choice(self.CORNERS)
        
        #If we can win, take position
        can_self_win = self.can_win(AI_list, taken_list)
        if (can_self_win != -1):
            return can_self_win
        
        #If enemy can win, block position
        can_enemy_win = self.can_win(player_list, taken_list)
        if (can_enemy_win != -1):
            return can_enemy_win
        
        
        #Otherwise, run minimax
        else:
            return self.minimax(AI_list, player_list, taken_list)
    
    
    def minimax(self, max_list, min_list, taken_list):
        canWinPos = self.can_win(max_list, taken_list)
        #If player can make a winning move from here, just make that move
        if (canWinPos != -1):
            return canWinPos
        #Otherwise, call run minimax algorithm 
        else:
            new_move_list = (self.generateStates(max_list, min_list, taken_list, True)[0])
            new_move = list(set(new_move_list).difference(set(max_list)))[0]
            return new_move
            
    def generateStates(self, current_list, enemy_list, taken_list, maximizingPlayer):
        #Base case:
        #If this move is a leaf, return a score
        if (len(taken_list) == 9):
            evalu = self.eval_board(current_list, enemy_list, taken_list)
            if (maximizingPlayer):
                return (current_list, evalu)
            else:
                return (current_list, (-1)*evalu)
                
        else:
            #new_states is list of all possible moves for current_list
            new_states = []
            new_taken_list = list(taken_list)
            while (len(new_taken_list) != 9):
                new_move = self.generate_move_easy(new_taken_list)
                new_taken_list.append(new_move)
                new_current_list = list(current_list)
                new_current_list.append(new_move)
                new_states.append(new_current_list)
                
            #for each new_states state, assign a score
            scored_states = []
            for state in new_states:
                state_set = set(state)
                taken_list_set = set(taken_list)
                new_move = list(state_set.difference(taken_list_set))[0]
                new_taken_list = list(taken_list)
                new_taken_list.append(new_move)
                score = (self.generateStates(enemy_list, state, new_taken_list, not(maximizingPlayer)))[1]
                scored_states.append((state,score))
                
            #choose the best-scoring state and return it
            if (maximizingPlayer):
                current_score = -1
                current_move = []
                for state in scored_states:
                    if (state[1] > current_score):
                        current_move = state[0]
                        current_score = state[1]
            else:
                current_score = 1
                current_move = []
                for state in scored_states:
                    if (state[1] < current_score):
                        current_move = state[0]
                        current_score = state[1]
            return (current_move, current_score)
        
            
    #Static board evaluation
    def eval_board(self, given_list, enemy_list, taken_list):
        if self.check_win(given_list):
            return 1
        elif self.check_win(enemy_list):
            return -1
        else:
            return 0
            
    #Check if a win is possible given a list of positions; 
    #If possible, return position; if not, return -1
    def can_win(self, given_list, taken_list):
        gset = set(given_list)
        tset = set(taken_list)
        for item in self.WIN_POSITION_LIST:
            wset = set(item)
            difference = wset.difference(gset)
            if ((len(difference) == 1) and (not(difference.issubset(tset)))):
                d = list(difference)
                return d[0]
        return -1
    
    def check_win(self, given_list):
        if (len(given_list) >= 3):
            for item in self.WIN_POSITION_LIST:
                    if item[0] in given_list and item[1] in given_list and item[2] in given_list: 
                            return True
            return False
    
    def change_difficulty(self, diff):
        if (diff == "Easy"):
            self.diff = "Easy"
        elif (diff == "Normal"):
            self.diff = "Normal"
        else:
            self.diff = "Hard"  
    
    def other_player(self, marker):
        if (marker == "x"):
            return "o"
        else:
            return "x"