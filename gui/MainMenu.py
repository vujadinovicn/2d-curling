import pygame
import sys
from helper import constants
from gui.Button import Button
from gui.TextArea import TextArea
from game.Parameters import Parameters
from game.Match import Match

pygame.init()


class MainMenu:
    """Class for non-game windows."""
    def __init__(self, screen):
        """
        Parameterized constructor creates all areas and button.
        :param screen: Surface where window is drawn.
        """
        self.screen = screen
        self.button_play = Button(self.screen, constants.button_image, 300, 320, "PLAY",
                                  constants.font, constants.navy_blue)
        self.mass_area = TextArea(self.screen, constants.button_image, 80, 74, "Mass (kg)",
                                  constants.font_start, constants.mass, constants.mass_range)
        self.mi_area = TextArea(self.screen, constants.button_image, 80, 164, "Mu (10^-2)",
                                constants.font_start, int(constants.mi * 100), constants.mi_range)
        self.rounds_area = TextArea(self.screen, constants.button_image, 80, 254, "No. of rounds",
                                    constants.font_start, constants.rounds, constants.rounds_range)
        self.stones_area = TextArea(self.screen, constants.button_image, 80, 344, "No. of stones",
                                    constants.font_start, constants.stones, constants.stones_range)
        self.button_start = Button(self.screen, constants.button_start_image, 490, 80, "Start",
                                   constants.font, constants.red_hover_start, constants.white)
        self.areas = []

    def append_areas(self):
        self.areas.append(self.mass_area)
        self.areas.append(self.mi_area)
        self.areas.append(self.rounds_area)
        self.areas.append(self.stones_area)

    def draw(self):
        self.button_start.draw()
        for area in self.areas:
            area.draw()

    def hover(self):
        """
        Method checks if widgets are hovered.
        """
        self.button_start.hover(pygame.mouse.get_pos())
        for area in self.areas:
            area.button_minus.hover(pygame.mouse.get_pos())
            area.button_plus.hover(pygame.mouse.get_pos())

    def pressed(self):
        """
        Method checks if areas buttons are pressed.
        """
        for area in self.areas:
            area.pressed()

    def screen_main(self):
        """
        Method for drawing the first window.
        Draws text, background and button for continuing.
        If button is clicked proceeds to next function.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play.pressed(pygame.mouse.get_pos()):
                        self.screen_start()
            self.screen.blit(constants.background_main, (0, 0))
            self.button_play.draw()
            self.button_play.hover(pygame.mouse.get_pos())
            self.screen.blit(constants.curling_text, constants.curling_rect)
            pygame.display.update()

    def screen_start(self):
        """
        Method for drawing the second window.
        Draws background, areas and button for starting the game.
        If button is pressed proceeds to start the game.
        """
        self.append_areas()
        while True:
            self.screen.blit(constants.background_start, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pressed()
                    if self.button_start.pressed(pygame.mouse.get_pos()):
                        surface = pygame.display.set_mode((500,730), pygame.RESIZABLE, pygame.SCALED)
                        parameters = Parameters(self.mass_area.value, self.mi_area.value,
                                                self.rounds_area.value, self.stones_area.value)  #gets all wanted parameters that user put
                        match = Match(surface, parameters)
                        match.run()
            self.draw()
            self.hover()
            pygame.display.update()


