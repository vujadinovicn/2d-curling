from helper import constants
import pygame
from gui.Button import Button


class TextArea:
    """Class for selecting the value of game's parameter."""
    def __init__(self, screen, image, x, y, text, font, value, range):
        """
        Parameterized constructor.
        :param screen: Surface where area is drawn.
        :param image: Back image of area.
        :param x: Position of area on x-axis.
        :param y: Position of area on y-axis.
        :param text: Name of game parameter.
        :param font: Font used for text.
        :param value: Inital value of game parameter.
        :param range: Possible values for game parameter
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.font = font
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text = self.font.render(text, True, constants.white)
        self.text_rect = self.text.get_rect(center=(self.x+22, self.y-38))
        self.input_rect = pygame.Rect(self.x-8, self.y - 20, 55, 40)
        self.button_minus = Button(self.screen, constants.button_pm_image, self.x - 23, self.y, "-", self.font, constants.red_hover_start)
        self.button_plus = Button(self.screen, constants.button_pm_image, self.x + 67, self.y, "+", self.font, constants.red_hover_start)
        self.value = value
        self.range = range

    def draw(self):
        self.screen.blit(self.text, self.text_rect)
        pygame.draw.rect(self.screen, constants.red_hover_start, self.input_rect)
        text = self.font.render(str(self.value), True, constants.white)
        dx = 0
        if len(str(self.value)) == 1:
            dx = 7
        self.screen.blit(text, (self.input_rect.x+15+dx,self.input_rect.y+6))
        self.button_plus.draw()
        self.button_minus.draw()

    def pressed(self):
        """
        Method for changing the value of parameter when the button is clicked.
        """
        if self.button_plus.pressed(pygame.mouse.get_pos()):
            self.value += 1
            if self.value > max(self.range):
                self.value = self.range[-1]
        if self.button_minus.pressed(pygame.mouse.get_pos()):
            self.value -= 1
            if self.value < min(self.range):
                self.value = self.range[0]