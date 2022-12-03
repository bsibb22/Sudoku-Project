from cell import Cell
from constants import *
import pygame

class Board:
  def __init__(self, width, height, screen, difficulty, board_size=9):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.cells = []

    self.board_size = board_size

    # add all the cells; where to change cell's values?
    for row in range(self.board_size):
      row_to_add = []
      for col in range(self.board_size):
        row_to_add.append(Cell(0, row, col, self.screen))
      self.cells.append(row_to_add)

  def draw(self):
    cell_width = BOARD_WIDTH / self.board_size
    cell_height = BOARD_HEIGHT / self.board_size

    top_left_corner = (SCREEN_WIDTH / 2 - self.width / 2, SCREEN_HEIGHT / 2 - self.height / 2)

    for i in range(self.board_size + 1):
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (top_left_corner[0] + cell_width * i, top_left_corner[1]),
            (top_left_corner[0] + cell_width * i, top_left_corner[1] + self.height),
            6 if i % 3 == 0 else 3
        )
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (top_left_corner[0], top_left_corner[1] + cell_height * i),
            (top_left_corner[0] + self.width, top_left_corner[1] + cell_height * i),
            6 if i % 3 == 0 else 3
        )

  def select(self, row, col):
    pass

  def click(self, x, y):
    """
    if x > board_x and x < board_x + board_width and y > board_y and y < board_y + board_height:
      return x // cell_width, y // cell_height
    """
    pass

  def clear(self):
    pass

  def sketch(self, value):
    pass

  def place_number(self, value):
    pass

  def reset_to_original(self):
    pass

  def is_full(self):
    pass

  def update_board(self):
    pass

  def find_empty(self):
    pass

  def check_board(self):
    pass
