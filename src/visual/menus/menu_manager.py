from src.visual.menus.passive_menus.positioning_menu import PositionMenu
from src.visual.menus.passive_menus.connections_menu import ConnectionMenu
from src.visual.menus.passive_menus.description_menu import DescriptionMenu
from src.visual.menus.passive_menus.icon_and_name_menu import IconNameMenu
from src.visual.menus.passive_menus.passive_type_menu import TypeMenu
from src.visual.menus.passive_menus.requirements_menu import RequirementsMenu
from src.visual.menus.passive_menus.edit_stats_menu import EditStatsMenu
from src.visual.menus.default_menu import DefaultMenu
from src.visual.menus.selected_passive_menu import SelectedPassiveMenu


# only check events for buttons when that menu is showing (else it multi triggers random events)


class MenuManager:
    def __init__(self, surface):
        self.surface = surface
        self.menus = {
            "Default": DefaultMenu(self),
            "Position": PositionMenu(self),
            "Type": TypeMenu(self),
            "Connections": ConnectionMenu(self),
            "Requirements": RequirementsMenu(self),
            "Edit_Stats": EditStatsMenu(self),
            "Icon_Name": IconNameMenu(self),
            "Description": DescriptionMenu(self),
            "Selected": SelectedPassiveMenu(self)
        }
        self.current_menu = "Default"

    def menu_events(self, mouse_position):
        self.menus[self.current_menu].menu_events(mouse_position)

    def draw_menu(self):
        self.menus[self.current_menu].draw_menu(self.surface)

