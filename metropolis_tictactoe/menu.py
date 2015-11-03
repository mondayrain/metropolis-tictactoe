'''
Code that runs the menu page
'''

import pygame
import constants
import webbrowser
import constants

class Menu:

    STATE_MAIN = 0
    STATE_ONE_PLAYER = 1
    STATE_TWO_PLAYER = 2
    STATE_ONLINE = 3
    STATE_SETTINGS = 4
    
    def __init__(self, screen):
        self.current_state = 0
        self.diff = "Normal"
        self.track = constants.TRACK_1[1]
        self.current_difficulty = constants.NORMAL
        self.difficulty_coor = constants.NORMAL_COOR
        self.current_track = constants.TRACK_ONE
        self.track_coor = constants.TRACK1_COOR
        self.waiting = False
        self.waiting_time = 30
    
    def run_menu_page(self, screen):
        while(self.current_state == 0):
            mouse_position = pygame.mouse.get_pos()
            mouse_click = (0,0)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.current_state = -1
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click = mouse_position

            self.draw_page(screen, mouse_position)
 
            try:
                self.menu_button_clicked(mouse_click[0], mouse_click[1])
            except:
                pass
            pygame.display.flip()
        
    def draw_menu_markers(self, screen):
        screen.blit(constants.ONE_PLAYER, constants.ONE_PLAYER_COOR)
        screen.blit(constants.TWO_PLAYER, constants.TWO_PLAYER_COOR)
        screen.blit(constants.ONLINE, constants.ONLINE_COOR)
        screen.blit(constants.SETTINGS, constants.SETTINGS_COOR)
        
    def draw_menu_markers_hover(self, screen, mouse_x, mouse_y):
        if (self.find_menu_position(mouse_x, mouse_y) == 1):
                screen.blit(constants.ONE_PLAYER_HOVER, constants.ONE_PLAYER_COOR)
        if (self.find_menu_position(mouse_x, mouse_y) == 2):
            if (constants.TWO_PLAYER_COOR[1] < mouse_y < constants.TWO_PLAYER_COOR[1] + constants.TWO_PLAYER.get_size()[1]): 
                screen.blit(constants.TWO_PLAYER_HOVER, constants.TWO_PLAYER_COOR)
        if (self.find_menu_position(mouse_x, mouse_y) == 3):
            if (constants.ONLINE_COOR[1] < mouse_y < constants.ONLINE_COOR[1] + constants.ONLINE.get_size()[1]): 
                screen.blit(constants.ONLINE_HOVER, constants.ONLINE_COOR)
        if (self.find_menu_position(mouse_x, mouse_y) == 4):
            if (constants.SETTINGS_COOR[1] < mouse_y < constants.SETTINGS_COOR[1] + constants.SETTINGS.get_size()[1]): 
                screen.blit(constants.SETTINGS_HOVER, constants.SETTINGS_COOR)
        
    def draw_credits(self, screen):
        screen.blit(constants.CREDITS_MUSIC, constants.CREDITS_MUSIC_COOR)
        screen.blit(constants.CREDITS_MUSIC_NAME, constants.CREDITS_MUSIC_NAME_COOR)
        screen.blit(constants.CREDITS_PHOTO, constants.CREDITS_PHOTO_COOR)
        screen.blit(constants.CREDITS_PHOTO_NAME, constants.CREDITS_PHOTO_NAME_COOR)
    
    def draw_credits_hover(self, screen, mouse_x, mouse_y):
        if (constants.CREDITS_MUSIC_HOVER_COOR[0] < mouse_x < constants.SCREEN_WIDTH):
            if (constants.CREDITS_MUSIC_HOVER_COOR[1] < mouse_y < constants.CREDITS_MUSIC_HOVER_COOR[1] + constants.CREDITS_MUSIC_HOVER.get_size()[1]):
                screen.blit(constants.CREDITS_MUSIC_HOVER, constants.CREDITS_MUSIC_HOVER_COOR)
        if (constants.CREDITS_PHOTO_HOVER_COOR[0] < mouse_x < constants.SCREEN_WIDTH):
            if (constants.CREDITS_PHOTO_HOVER_COOR[1] < mouse_y < constants.SCREEN_HEIGHT):
                screen.blit(constants.CREDITS_PHOTO_HOVER, constants.CREDITS_PHOTO_HOVER_COOR)    

    def draw_page(self, screen, mouse_position=(0,0)):
        screen.blit(constants.BACKGROUND, (0,0))
        screen.blit(constants.HEADING, constants.HEADING_COORDINATES)
        screen.blit(constants.TITLE, constants.TITLE_COORDINATES)
        self.draw_menu_markers(screen)
        self.draw_menu_markers_hover(screen, mouse_position[0], mouse_position[1])

        self.draw_credits(screen)
        self.draw_credits_hover(screen, mouse_position[0], mouse_position[1])

    def draw_message(self, screen, message):
       """
       Draw a message over the current screen/gameboard.
       TODO: This is duplicate code of Game.draw_message.
             Should figure out a way to pull this out.
       """
       text = constants.MESSAGE_FONT.render(message, 1, (255, 255, 255))
       textcoordinates = ((constants.SCREEN_WIDTH - text.get_size()[0])/2, (constants.TITLE_COORDINATES[1] + 45))

       screen.blit(text, textcoordinates)
        
    # Check if current mouse position is over a button
    # 1 = 1P, 2 = 2P, 3 = Online, 4 = Settings, 5 = Scott, 6= Stephen
    def find_menu_position(self, mouse_x, mouse_y):
        if (constants.ONE_PLAYER_COOR[0] < mouse_x < constants.ONE_PLAYER_COOR[0] + constants.ONE_PLAYER.get_size()[0]):
            if (constants.ONE_PLAYER_COOR[1] < mouse_y < constants.ONE_PLAYER_COOR[1] + constants.ONE_PLAYER.get_size()[1]): 
                return 1
        if (constants.TWO_PLAYER_COOR[0] < mouse_x < constants.TWO_PLAYER_COOR[0] + constants.TWO_PLAYER.get_size()[0]):
            if (constants.TWO_PLAYER_COOR[1] < mouse_y < constants.TWO_PLAYER_COOR[1] + constants.TWO_PLAYER.get_size()[1]): 
                return 2
        if (constants.ONLINE_COOR[0] < mouse_x < constants.ONLINE_COOR[0] + constants.ONLINE.get_size()[0]):
            if (constants.ONLINE_COOR[1] < mouse_y < constants.ONLINE_COOR[1] + constants.ONLINE.get_size()[1]): 
                return 3
        if (constants.SETTINGS_COOR[0] < mouse_x < constants.SETTINGS_COOR[0] + constants.SETTINGS.get_size()[0]):
            if (constants.SETTINGS_COOR[1] < mouse_y < constants.SETTINGS_COOR[1] + constants.SETTINGS.get_size()[1]): 
                return 4
        if (constants.CREDITS_MUSIC_HOVER_COOR[0] < mouse_x < constants.SCREEN_WIDTH):
            if (constants.CREDITS_MUSIC_HOVER_COOR[1] < mouse_y < constants.CREDITS_MUSIC_HOVER_COOR[1] + constants.CREDITS_MUSIC_HOVER.get_size()[1]):
                return 5
        if (constants.CREDITS_PHOTO_HOVER_COOR[0] < mouse_x < constants.SCREEN_WIDTH):
            if (constants.CREDITS_PHOTO_HOVER_COOR[1] < mouse_y < constants.SCREEN_HEIGHT):
                return 6
        
    def menu_button_clicked(self, mouse_x, mouse_y):
        
        if (self.find_menu_position(mouse_x, mouse_y) == 1):
            self.current_state = 1
            
        if (self.find_menu_position(mouse_x, mouse_y) == 2):
            self.current_state = 2

        if (self.find_menu_position(mouse_x, mouse_y) == 3):
            self.current_state = 3
        
        if (self.find_menu_position(mouse_x, mouse_y) == 4):
            self.current_state = 4
        
        if (self.find_menu_position(mouse_x, mouse_y) == 5):
            webbrowser.open("http://www.scottstedman.com/category/music/", new=0, autoraise=True)
            
        if (self.find_menu_position(mouse_x, mouse_y) == 6):
            webbrowser.open("http://disco--very.tumblr.com/", new=0, autoraise=True)
        
    def run_settings_page(self, screen):
        while(self.current_state == 4):
            mouse_position = pygame.mouse.get_pos()
            mouse_click = (0,0)
            click_happened = False
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.current_state = -1
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click = mouse_position
                    click_happened = True
                              
            screen.blit(constants.BACKGROUND, (0,0))
            screen.blit(constants.HEADING, constants.HEADING_COORDINATES)
            screen.blit(constants.TITLE, constants.TITLE_COORDINATES)
            self.draw_settings_markers(screen)
            self.draw_settings_hover(screen, mouse_position[0], mouse_position[1])
            if (click_happened):
                self.settings_button_clicked(mouse_click[0], mouse_click[1])
            pygame.display.flip()
    
    def draw_settings_markers(self, screen):
        #Draw words
        screen.blit(constants.DIFFICULTY, constants.DIFFICULTY_COOR)
        screen.blit(constants.MUSIC, constants.MUSIC_COOR)
        screen.blit(self.current_difficulty, self.difficulty_coor)
        screen.blit(self.current_track, self.track_coor)
        #Draw arrows
        screen.blit(constants.LEFT_ARROW, (self.difficulty_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0],
                                            self.difficulty_coor[1]))
        screen.blit(constants.RIGHT_ARROW, (self.difficulty_coor[0] + constants.ARROW_OFFSET + self.current_difficulty.get_size()[0],
                                            self.difficulty_coor[1]))
        screen.blit(constants.LEFT_ARROW, (self.track_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0],
                                            self.track_coor[1]))
        screen.blit(constants.RIGHT_ARROW, (self.track_coor[0] + constants.ARROW_OFFSET + self.current_track.get_size()[0],
                                            self.track_coor[1]))
        screen.blit(constants.BACK_ARROW, ((constants.SCREEN_WIDTH - constants.BACK_ARROW.get_size()[0])/2, 
                                           self.track_coor[1] + constants.SETTINGS_OFFSET*2 + constants.MENU_OFFSET))
    
    def draw_settings_hover(self, screen, mouse_x, mouse_y):
        if (self.find_settings_position(mouse_x, mouse_y) == 1):
            screen.blit(constants.LEFT_ARROW_HOVER, (self.difficulty_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0],
                                            self.difficulty_coor[1]))
        if (self.find_settings_position(mouse_x, mouse_y) == 2):
            screen.blit(constants.RIGHT_ARROW_HOVER, (self.difficulty_coor[0] + constants.ARROW_OFFSET + self.current_difficulty.get_size()[0],
                                            self.difficulty_coor[1]))
        if (self.find_settings_position(mouse_x, mouse_y) == 3):
            screen.blit(constants.LEFT_ARROW_HOVER, (self.track_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0],
                                            self.track_coor[1]))
        if (self.find_settings_position(mouse_x, mouse_y) == 4):
            screen.blit(constants.RIGHT_ARROW_HOVER, (self.track_coor[0] + constants.ARROW_OFFSET + self.current_track.get_size()[0],
                                            self.track_coor[1]))
        if (self.find_settings_position(mouse_x, mouse_y) == 5):
            screen.blit(constants.BACK_ARROW_HOVER, ((constants.SCREEN_WIDTH - constants.BACK_ARROW.get_size()[0])/2, 
                                           self.track_coor[1] + constants.SETTINGS_OFFSET*2 + constants.MENU_OFFSET))
            
    
    def settings_button_clicked(self, mouse_x, mouse_y):
        if (self.find_settings_position(mouse_x, mouse_y) == 1):
            self.prev_difficulty()
        if (self.find_settings_position(mouse_x, mouse_y) == 2):
            self.next_difficulty()
        if (self.find_settings_position(mouse_x, mouse_y) == 3):
            self.prev_track()
        if (self.find_settings_position(mouse_x, mouse_y) == 4):
            self.next_track()
        if (self.find_settings_position(mouse_x, mouse_y) == 5):
            self.current_state = 0
    # Check if current mouse position is over an arrow
    # 1 = difficulty left arrow, 2 = difficulty right arrow, 3 = music left arrow, 4 = music right arrow, 5 = back
    def find_settings_position(self, mouse_x, mouse_y):
        if ((self.difficulty_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0]) < mouse_x 
            < self.difficulty_coor[0] + constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0] + constants.LEFT_ARROW.get_size()[0]):
            if(self.difficulty_coor[1] < mouse_y < self.difficulty_coor[1] + constants.LEFT_ARROW.get_size()[1]):
                return 1
        if ((self.difficulty_coor[0] + self.current_difficulty.get_size()[0] + constants.ARROW_OFFSET) < mouse_x 
            < (self.difficulty_coor[0] + self.current_difficulty.get_size()[0] + constants.ARROW_OFFSET + constants.LEFT_ARROW.get_size()[0])):
            if(self.difficulty_coor[1] < mouse_y < self.difficulty_coor[1] + constants.RIGHT_ARROW.get_size()[1]):
                return 2
        if ((self.track_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0]) < mouse_x 
            < self.track_coor[0] - constants.ARROW_OFFSET - constants.LEFT_ARROW.get_size()[0] + constants.LEFT_ARROW.get_size()[0]):
            if (self.track_coor[1] < mouse_y < self.track_coor[1] + constants.LEFT_ARROW.get_size()[1]):
                return 3
        if ((self.track_coor[0] + self.current_track.get_size()[0] + constants.ARROW_OFFSET) < mouse_x 
            < (self.track_coor[0] + self.current_track.get_size()[0] + constants.ARROW_OFFSET + constants.LEFT_ARROW.get_size()[0])):
            if(self.track_coor[1] < mouse_y < self.track_coor[1] + constants.RIGHT_ARROW.get_size()[1]):
                return 4
        if ((constants.SCREEN_WIDTH - constants.BACK_ARROW.get_size()[0])/2 < mouse_x <
            (constants.SCREEN_WIDTH - constants.BACK_ARROW.get_size()[0])/2 + constants.BACK_ARROW.get_size()[0]):
            if ((self.track_coor[1] + constants.SETTINGS_OFFSET + constants.MENU_OFFSET) < mouse_y <
                (self.track_coor[1] + constants.SETTINGS_OFFSET + constants.MENU_OFFSET + constants.BACK_ARROW.get_size()[1])):
                return 5
    
    def next_difficulty(self):
        if (self.current_difficulty == constants.EASY):
            self.diff = "Normal"
            self.current_difficulty = constants.NORMAL
            self.difficulty_coor = constants.NORMAL_COOR
        elif (self.current_difficulty == constants.NORMAL):
            self.diff = "Hard"
            self.current_difficulty = constants.HARD
            self.difficulty_coor = constants.HARD_COOR
        else:
            self.diff = "Easy"
            self.current_difficulty = constants.EASY
            self.difficulty_coor = constants.EASY_COOR
            
    def prev_difficulty(self):
        if (self.current_difficulty == constants.EASY):
            self.diff = "Hard"
            self.current_difficulty = constants.HARD
            self.difficulty_coor = constants.HARD_COOR
        elif (self.current_difficulty == constants.NORMAL):
            self.diff = "Easy"
            self.current_difficulty = constants.EASY
            self.difficulty_coor = constants.EASY_COOR
        else:
            self.diff = "Normal"
            self.current_difficulty = constants.NORMAL
            self.difficulty_coor = constants.NORMAL_COOR
            
    def next_track(self):
        if (self.current_track == constants.TRACK_ONE):
            self.track = constants.TRACK_2[1]
            self.current_track = constants.TRACK_TWO
            self.track_coor = constants.TRACK2_COOR
        elif (self.current_track == constants.TRACK_TWO):
            self.track = constants.TRACK_3[1]
            self.current_track = constants.TRACK_THREE
            self.track_coor = constants.TRACK3_COOR
        else:
            self.track = constants.TRACK_1[1]
            self.current_track = constants.TRACK_ONE
            self.track_coor = constants.TRACK1_COOR
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(-1)
            
    def prev_track(self):
        if (self.current_track == constants.TRACK_ONE):
            self.track = constants.TRACK_3[1]
            self.current_track = constants.TRACK_THREE
            self.track_coor = constants.TRACK3_COOR
        elif (self.current_track == constants.TRACK_TWO):
            self.track = constants.TRACK_1[1]
            self.current_track = constants.TRACK_ONE
            self.track_coor = constants.TRACK1_COOR
        else:
            self.track = constants.TRACK_2[1]
            self.current_track = constants.TRACK_TWO
            self.track_coor = constants.TRACK2_COOR
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(-1)
