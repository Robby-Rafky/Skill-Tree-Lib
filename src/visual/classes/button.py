from src.visual.classes.text_box import *


class Button(TextBox):
    """Represents a button in the game.

    The Button class extends the TextBox class and provides functionality for creating interactive buttons.

    Attributes:
        rect (pygame.Rect): The rectangular area enclosing the button.

    Methods:
        __init__(text, position, size, offset, outline, centered, font_size, colour=GREY):
            Initializes a new instance of the Button class.
        update_button(text, colour):
            Updates the text and colour of the button.
        update_button_position(text, colour, x, y):
            Updates the position, text, and colour of the button.
        button_event(mouse_coordinates):
            Checks if a button event has occurred.

    """

    def __init__(self, text, position, size, colour=(235, 169, 94)):
        """
        Initializes a new instance of the Button class.

        Args:
            text (str): The text displayed on the button.
            position (tuple): The position of the button (x, y).
            size (tuple): The size of the button (width, height).
            colour (tuple, optional): The colour of the button. Defaults to GREY.
        """
        TextBox.__init__(self, text, position, size, centered=True, colour=colour)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def update_button(self, text, colour):
        """
        Updates the text and colour of the button.

        Args:
            text (str): The new text for the button.
            colour (tuple): The new colour for the button.
        """
        self.update_textbox(text, colour)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def update_button_position(self, text, colour, x, y):
        """
        Updates the position, text, and colour of the button.

        Args:
            text (str): The new text for the button.
            colour (tuple): The new colour for the button.
            x (int): The new x-coordinate of the button.
            y (int): The new y-coordinate of the button.
        """
        self.x, self.y = x, y
        self.update_button(text, colour)

    def button_event(self, mouse_coordinates):
        """
        Checks if a button event has occurred.

        Args:
            mouse_coordinates (tuple): The coordinates of the mouse (x, y).

        Returns:
            bool: True if a button event has occurred, False otherwise.
        """
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_coordinates):
                return True
            return False
