from src.visual.classes.button import Button


class DefaultMenu:
    def __init__(self, menu_manager_ref):
        self.menu_manage_ref = menu_manager_ref
        self.button_create_passive = Button("Create Passive", (40, 40), (400, 140))
        self.button_save_skill_tree = Button("Save Skill Tree", (1480, 40), (400, 60))
        self.button_load_skill_tree = Button("Load Skill Tree", (1480, 120), (400, 60))

    def menu_events(self, mouse_position):
        if self.button_create_passive.button_event(mouse_position):
            self.menu_manage_ref.current_menu = "Position"

    def draw_menu(self, surface):
        self.button_create_passive.draw_on_surface(surface)
        self.button_save_skill_tree.draw_on_surface(surface)
        self.button_load_skill_tree.draw_on_surface(surface)
