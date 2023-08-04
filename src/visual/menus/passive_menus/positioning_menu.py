from src.visual.classes.button import Button
#required

class PositionMenu:
    def __init__(self, menu_manager_ref):
        self.button_create_passive = Button("beans", (40, 40), (400, 140))
        self.button_save_skill_tree = Button("beans", (1280, 40), (400, 60))
        self.button_load_skill_tree = Button("beans", (1180, 120), (400, 60))

    def menu_events(self, mouse_position):
        if self.button_create_passive.button_event(mouse_position):
            print("ye")

    def draw_menu(self, surface):
        self.button_create_passive.draw_on_surface(surface)
        self.button_save_skill_tree.draw_on_surface(surface)
        self.button_load_skill_tree.draw_on_surface(surface)
