from src.visual.colours_imports import *
from src.visual.menus.menu_manager import MenuManager
from src.visual.skill_tree.skill_tree import SkillTreeSurface


class BaseWindow:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.mouse_pos = (0, 0)
        self.base_surface = pygame.Surface((1920, 1080))
        self.window = pygame.display.set_mode((1920, 1080))
        self.menu_manager = MenuManager(self.base_surface)
        self.skill_tree_surface = SkillTreeSurface()

    def draw_layers(self):
        self.base_surface.fill(GREY)

        pygame.draw.line(self.base_surface, BLACK, (0, 220), (1920, 220), width=3)

        self.skill_tree_surface.draw_skill_tree(self.base_surface)
        self.menu_manager.draw_menu()

        self.window.blit(self.base_surface, (0, 0))

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.menu_manager.menu_events(self.mouse_pos)

    def window_loop(self):
        self.mouse_pos = pygame.mouse.get_pos()

        self.event_check()
        self.draw_layers()

        self.clock.tick(60)
        pygame.display.flip()

