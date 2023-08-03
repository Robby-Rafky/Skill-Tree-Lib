from src.visual.colours_imports import *
from src.visual.classes.button import Button
from src.visual.bottom_menu.bottom_menu import BottomMenu


class BaseWindow:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.mouse_pos = (0, 0)
        self.base_surface = pygame.Surface((1920, 1080))
        self.window = pygame.display.set_mode((1920, 1080))
        self.bottom_menu = BottomMenu(self.base_surface)

    def draw_layers(self):
        self.base_surface.fill((67, 67, 67))

        pygame.draw.line(self.base_surface, BLACK, (0, 920), (1920, 920), width=3)

        pygame.draw.line(self.base_surface, BLACK, (0, 220), (1920, 220), width=3)

        self.bottom_menu.draw_menu(True)

        self.window.blit(self.base_surface, (0, 0))

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def window_loop(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.event_check()
        self.draw_layers()

        self.clock.tick(60)
        pygame.display.flip()

