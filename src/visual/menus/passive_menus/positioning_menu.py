from src.visual.colours_imports import *
from src.visual.classes.button import Button
from src.visual.classes.text_box import TextBox
#required

class PositionMenu:
    def __init__(self, menu_manager_ref):
        self.menu_manage_ref = menu_manager_ref
        self.positioning_info = TextBox(" ", (40, 40), (600, 70), False)
        self.passive_position = TextBox("Current Passive Location: (_, _) ", (40, 130), (600, 50), False)
        self.button_move_up = Button("↑", (940, 20), (80, 80))
        self.button_move_down = Button("↓", (940, 120), (80, 80))
        self.button_move_left = Button("←", (840, 70), (80, 80))
        self.button_move_right = Button("→", (1040, 70), (80, 80))
        self.button_submit_position = Button("Lock In Position", (1480, 40), (400, 140))

        self.positioning_info.update_textbox_multiline(["Select the location of the passive,",
                                                       "use the arrows to move the passive by 1 unit."], L_GREY)

    def menu_events(self, mouse_position):
        if self.button_move_up.button_event(mouse_position):
            print("up")
        if self.button_move_down.button_event(mouse_position):
            print("down")
        if self.button_move_left.button_event(mouse_position):
            print("left")
        if self.button_move_right.button_event(mouse_position):
            print("right")
        if self.button_submit_position.button_event(mouse_position):
            self.menu_manage_ref.current_menu = "Type"

    def draw_menu(self, surface):
        self.positioning_info.draw_on_surface(surface)
        self.passive_position.draw_on_surface(surface)
        self.button_move_up.draw_on_surface(surface)
        self.button_move_down.draw_on_surface(surface)
        self.button_move_left.draw_on_surface(surface)
        self.button_move_right.draw_on_surface(surface)
        self.button_submit_position.draw_on_surface(surface)
