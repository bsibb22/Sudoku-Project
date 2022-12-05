from constants import *
import pygame


class Cell:
    def __init__(self, value, row, col, screen, tl_corner=(0, 0)):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

        self.tl_corner = tl_corner
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if not self.value == 0:
            value_font = pygame.font.Font(None, 60)
            value_surf = value_font.render(str(self.value), 0, (0, 0, 0))
            value_rect = value_surf.get_rect(
                center=(
                    CELL_WIDTH * self.col + CELL_WIDTH // 2 + self.tl_corner[0],
                    CELL_HEIGHT * self.row + CELL_HEIGHT // 2 + self.tl_corner[1]))
            self.screen.blit(value_surf, value_rect)
