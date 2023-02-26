from helper import constants


class Button:
    """Class for action handling."""
    def __init__(self, screen, image, x, y, text, font, hover_color, color = constants.blue_main):
        """
        Parameterized constructor.
        :param screen: Surface where area is drawn.
        :param image: Back image of button.
        :param x: Position of button on x-axis.
        :param y: Position of button on y-axis.
        :param text: Button meaning.
        :param font: Font used for text.
        :param hover_color: Color of text when button is hovered.
        :param color: Initial color of text.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.font = font
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.old_text = text
        self.color = color
        self.hover_color = hover_color
        self.text = self.font.render(text, True, self.color)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)

    def pressed(self, position):
        """
        Method checks if button is pressed.
        :param position: Position of the mouse.
        :return: (bool) True if button is pressed, False if not.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def hover(self, position):
        """
        Method checks if button is hovered.
        Changes the color of text if True.
        :param position: position of the mouse.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.old_text, True, self.hover_color)
        else:
            self.text = self.font.render(self.old_text, True, self.color)
