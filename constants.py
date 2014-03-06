'''
Constants used by several classes
'''

import os
import pygame
pygame.init()
pygame.font.init()

#SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DIR = os.path.dirname(__file__)


#Music
TRACK_1 = ("Superluminal", os.path.join(DIR, "music\\Superluminal.ogg"))
TRACK_2 = ("Any Means Necessary", os.path.join(DIR, "music\\Any_Means_Necessary.ogg"))
TRACK_3 = ("Isham House Track", os.path.join(DIR, "music\\Isham_House_Track.ogg"))

#Gameplay constants
WIN_POSITION_LIST = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), 
                     (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
TILE_DIMENSION = 100

#Fonts/Text surfaces
HEADING_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Metropolis1920.ttf"), 100)
TITLE_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Light.ttf"), 20)
MARKER_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Light.ttf"), 85)
MENU_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Light.ttf"), 25)
HEADING = HEADING_FONT.render("METROPOLIS", 1, (255, 255, 255))
TITLE = TITLE_FONT.render("T I C   T A C   T O E", 1, (255, 255, 255))
ONE_PLAYER = MENU_FONT.render("1P Game", 1, (175, 175, 175))
TWO_PLAYER = MENU_FONT.render("2P Game", 1, (175, 175, 175))
ONLINE = MENU_FONT.render("Local Network Play", 1, (175, 175, 175))
SETTINGS = MENU_FONT.render("Settings", 1, (175, 175, 175))
ONE_PLAYER_HOVER = MENU_FONT.render("1P Game", 1, (255, 255, 255))
TWO_PLAYER_HOVER = MENU_FONT.render("2P Game", 1, (255, 255, 255))
ONLINE_HOVER = MENU_FONT.render("Local Network Play", 1, (255, 255, 255))
SETTINGS_HOVER = MENU_FONT.render("Settings", 1, (255, 255, 255))

CREDITS_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Light.ttf"), 14)
CREDITS_FONT_BOLD = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Bold.ttf"), 13)
CREDITS_MUSIC = CREDITS_FONT.render("Music by                          ", 1, (175, 175, 175))
CREDITS_PHOTO = CREDITS_FONT.render("Photography by                             ", 1, (175, 175, 175))
CREDITS_MUSIC_NAME = CREDITS_FONT_BOLD.render("Scott Stedman", 1, (175, 175, 175))
CREDITS_PHOTO_NAME = CREDITS_FONT_BOLD.render("Stephen Morgan", 1, (175, 175, 175))
CREDITS_MUSIC_HOVER = CREDITS_FONT_BOLD.render("Scott Stedman", 1, (255, 255, 255))
CREDITS_PHOTO_HOVER = CREDITS_FONT_BOLD.render("Stephen Morgan", 1, (255, 255, 255))

OPTIONS_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Light.ttf"), 20)
DIFFICULTY = MENU_FONT.render("Difficulty", 1, (255, 255, 255))
MUSIC = MENU_FONT.render("Music", 1, (255, 255, 255))
EASY = OPTIONS_FONT.render("Easy", 1, (175, 175, 175))
NORMAL = OPTIONS_FONT.render("Normal", 1, (175, 175, 175))
HARD = OPTIONS_FONT.render("Hard", 1, (175, 175, 175))
TRACK_ONE = OPTIONS_FONT.render(TRACK_1[0], 1, (175, 175, 175))
TRACK_TWO = OPTIONS_FONT.render(TRACK_2[0], 1, (175, 175, 175))
TRACK_THREE = OPTIONS_FONT.render(TRACK_3[0], 1, (175, 175, 175))


#Images
BACKGROUND = pygame.image.load(os.path.join(DIR, "images\\background.bmp"))
BOARD_SURFACE = pygame.image.load(os.path.join(DIR, "images\\board.bmp"))
EX = MARKER_FONT.render("X", 1, (0,0,0))
OH = MARKER_FONT.render("O", 1, (0,0,0))
HOVER_EX = MARKER_FONT.render("X", 1, (34, 34, 34,))
HOVER_OH = MARKER_FONT.render("O", 1, (34, 34, 34))
WINNING_EX = MARKER_FONT.render("X", 1, (255,255,255))
WINNING_OH = MARKER_FONT.render("O", 1, (255, 255, 255))
BOARD_SURFACE = pygame.image.load(os.path.join(DIR, "images\\board.bmp"))
ARROW_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Bold.ttf"), 24)
BACK_ARROW_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Bold.ttf"), 40)
RESET_FONT = pygame.font.Font(os.path.join(DIR, "fonts\\Nexa_Bold.ttf"), 40)
LEFT_ARROW = ARROW_FONT.render("<<", 1, (135, 135, 135))
RIGHT_ARROW = ARROW_FONT.render(">>", 1, (135, 135, 135))
BACK_ARROW = BACK_ARROW_FONT.render("<-", 1, (135, 135, 135))
RESET = RESET_FONT.render("o", 1, (135, 135, 135))
LEFT_ARROW_HOVER = ARROW_FONT.render("<<", 1, (255, 255, 255))
RIGHT_ARROW_HOVER = ARROW_FONT.render(">>", 1, (255, 255, 255))
BACK_ARROW_HOVER = BACK_ARROW_FONT.render("<-", 1, (255, 255, 255))
RESET_HOVER = RESET_FONT.render("o", 1, (255, 255, 255))


#/Offsets
MENU_OFFSET = 33
SETTINGS_OFFSET = 10
ARROW_OFFSET = 15

#Co-ordinates
BOARD_COORDINATES = ((SCREEN_WIDTH - BOARD_SURFACE.get_size()[0])/2, SCREEN_HEIGHT/2 - 50)
HEADING_COORDINATES = ((SCREEN_WIDTH - HEADING.get_size()[0])/2, 80)
TITLE_COORDINATES = ((SCREEN_WIDTH - TITLE.get_size()[0])/2, 75 + HEADING.get_size()[1])
ONE_PLAYER_COOR = ((SCREEN_WIDTH - ONE_PLAYER.get_size()[0])/2, (SCREEN_WIDTH - (TITLE_COORDINATES[1] + TITLE.get_size()[1]))/2-35)
TWO_PLAYER_COOR = ((SCREEN_WIDTH - TWO_PLAYER.get_size()[0])/2, ONE_PLAYER_COOR[1] + MENU_OFFSET)
ONLINE_COOR = ((SCREEN_WIDTH - ONLINE.get_size()[0])/2,TWO_PLAYER_COOR[1] + MENU_OFFSET)
SETTINGS_COOR = ((SCREEN_WIDTH - SETTINGS.get_size()[0])/2, ONLINE_COOR[1] + MENU_OFFSET)
CREDITS_MUSIC_COOR = (SCREEN_WIDTH - CREDITS_MUSIC.get_size()[0] - 10, SCREEN_HEIGHT - CREDITS_MUSIC.get_size()[1]*2 - 3)
CREDITS_PHOTO_COOR = (SCREEN_WIDTH - CREDITS_PHOTO.get_size()[0] - 10, SCREEN_HEIGHT - CREDITS_PHOTO.get_size()[1])
CREDITS_MUSIC_NAME_COOR = (SCREEN_WIDTH - CREDITS_MUSIC_NAME.get_size()[0] - 10, SCREEN_HEIGHT - CREDITS_MUSIC_NAME.get_size()[1]*2 - 3)
CREDITS_PHOTO_NAME_COOR = (SCREEN_WIDTH - CREDITS_PHOTO_NAME.get_size()[0] - 10, SCREEN_HEIGHT - CREDITS_PHOTO_NAME.get_size()[1])
CREDITS_MUSIC_HOVER_COOR = (SCREEN_WIDTH - CREDITS_MUSIC_HOVER.get_size()[0] - 10, SCREEN_HEIGHT - CREDITS_MUSIC_HOVER.get_size()[1]*2 - 3)
CREDITS_PHOTO_HOVER_COOR = (SCREEN_WIDTH - CREDITS_PHOTO_HOVER.get_size()[0] - 10, SCREEN_HEIGHT - CREDITS_PHOTO_HOVER.get_size()[1])
DIFFICULTY_COOR = ((SCREEN_WIDTH - DIFFICULTY.get_size()[0])/2, ONE_PLAYER_COOR[1])
MUSIC_COOR = ((SCREEN_WIDTH - MUSIC.get_size()[0])/2, DIFFICULTY_COOR[1]+DIFFICULTY.get_size()[1]+EASY.get_size()[1] + SETTINGS_OFFSET*2 + MENU_OFFSET)
EASY_COOR = ((SCREEN_WIDTH - EASY.get_size()[0])/2, DIFFICULTY_COOR[1] + DIFFICULTY.get_size()[1] + SETTINGS_OFFSET)
NORMAL_COOR = ((SCREEN_WIDTH - NORMAL.get_size()[0])/2, DIFFICULTY_COOR[1] + DIFFICULTY.get_size()[1] + SETTINGS_OFFSET)
HARD_COOR = ((SCREEN_WIDTH - HARD.get_size()[0])/2, DIFFICULTY_COOR[1] + DIFFICULTY.get_size()[1] + SETTINGS_OFFSET)
TRACK1_COOR = ((SCREEN_WIDTH - TRACK_ONE.get_size()[0])/2, MUSIC_COOR[1] + MUSIC.get_size()[1] + SETTINGS_OFFSET)
TRACK2_COOR = ((SCREEN_WIDTH - TRACK_TWO.get_size()[0])/2, MUSIC_COOR[1] + MUSIC.get_size()[1] + SETTINGS_OFFSET)
TRACK3_COOR = ((SCREEN_WIDTH - TRACK_THREE.get_size()[0])/2, MUSIC_COOR[1] + MUSIC.get_size()[1] + SETTINGS_OFFSET)
GAME_BACK_ARROW_COOR = (SCREEN_WIDTH/2 + (BOARD_SURFACE.get_size()[0])/2 + ARROW_OFFSET*2,
                                                BOARD_COORDINATES[1] + BOARD_SURFACE.get_size()[1] - ARROW_OFFSET*1.5)
GAME_RESET_COOR = (GAME_BACK_ARROW_COOR[0]+3, GAME_BACK_ARROW_COOR[1] - ARROW_OFFSET*3)



