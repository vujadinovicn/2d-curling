import pygame
from gui.MainMenu import MainMenu

if __name__ == '__main__':
    screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    menu = MainMenu(screen)
    menu.screen_main()


