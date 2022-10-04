import pygame

pygame.init()
pygame.display.set_icon(pygame.image.load('data/logo.jpg'))
pygame.mixer.init()
pygame.mixer.music.load("data/squid.mp3")

#background for first two windows
background_main = pygame.transform.scale(pygame.image.load("data/pozadina.jpg"), (600, 400))
background_start = pygame.transform.scale(pygame.image.load("data/pozadina2.jpg"), (600, 400))

#fonts
font_start = pygame.font.Font("data/font.ttf", 20)  #small font
font = pygame.font.Font("data/font.ttf", 40)  #medium font
main_font = pygame.font.Font("data/font.ttf", 80) #big font

#title text
curling_text = main_font.render("CURLING", True, (1, 93, 189))
curling_rect = curling_text.get_rect(center=(300,60))

#images
button_image = pygame.transform.scale(pygame.image.load("data/white.png"), (150, 35))  #white background.
button_start_image = pygame.transform.scale(pygame.image.load("data/blue.jpg"), (150, 35))  #blue background.
button_pm_image = pygame.transform.scale(pygame.image.load("data/white.png"), (40, 40))  #white background, smaller size.
winner_image = pygame.transform.scale(pygame.image.load("data/winner.png"), (300,300))  #trophy image.
tied_image = pygame.transform.scale(pygame.image.load("data/tied.png"), (300,300))

#initial values of parameters
mass = 18
rounds = 1
stones = 3
mi = 0.03
gravity = 10
radius = 15

#ranges of parameters
mass_range = [15, 21]
rounds_range = [1, 4]
stones_range = [3, 4]
mi_range = [2, 5]

#positions of curling's field
border_left = 100
border_right = 400
border_up = 0
border_down = 730

#starting position for stone
start_x = 250
start_y = 650

#home's center position
center = [250,150]

#positions of text when score is displayed
round_score_x = 125
round_score_h_y = 320
round_score_a_y = 360

#colors
white = (255, 255, 255)
red_hover_start = (202, 17, 35)
navy_blue = (0,0,128)
blue_main = (1, 93, 189)
yellow = (255,255,0)
green = (0,202,0)

#connection between colors and players
color_player = {green: "home", yellow: "away"}

#game screen
game_screen_w = 500
game_screen_h = 730
game_screen = pygame.display.set_mode((500, 730))