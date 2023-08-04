from src.visual.colours_imports import *

# TODO
# ADD "CURRENTLY SELECTED" (NAME/ID) TO THE BOTTOM OF THE SKILL TREE UI


class SkillTreeSurface:
    def __init__(self):
        self.tree_surface = pygame.Surface((1840, 750))
        self.bottom_ui_surface = pygame.Surface((1840, 50))

    def draw_skill_tree(self, surface):
        self.bottom_ui_surface.fill(L_GREY)
        self.tree_surface.fill(MENU_GREY)

        pygame.draw.rect(self.bottom_ui_surface, BLACK, (0, -4, 1840, 54), 4)
        pygame.draw.rect(self.tree_surface, BLACK, (0, 0, 1840, 750), 4)

        surface.blit(self.bottom_ui_surface, (40, 1000))
        surface.blit(self.tree_surface, (40, 250))

