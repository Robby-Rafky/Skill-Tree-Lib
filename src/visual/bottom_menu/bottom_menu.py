from src.visual.classes.button import Button


class BottomMenu:
    def __init__(self, surface):
        self.surface = surface
        # Only Visible When Passive Is Selected
        self.button_edit = Button("Edit Selected Passive", (40, 940), (500, 50))
        self.button_delete = Button("Delete Selected Passive", (730, 940), (500, 50))
        self.button_duplicate = Button("Duplicate Selected Passive", (1380, 940), (500, 50))

        # Always Visible
        self.button_create = Button("Create New Passive", (40, 1010), (500, 50))
        self.button_save_tree = Button("Save Skill Tree", (1380, 1010), (500, 50))

    def bottom_menu_events(self):
        pass

    def draw_menu(self, passive_selected):
        if passive_selected:
            self.button_edit.draw_on_surface(self.surface)
            self.button_delete.draw_on_surface(self.surface)
            self.button_duplicate.draw_on_surface(self.surface)
        self.button_create.draw_on_surface(self.surface)
        self.button_save_tree.draw_on_surface(self.surface)
