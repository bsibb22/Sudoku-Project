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
    self.matrix = [[]]

    self.board_size = board_size

    self.top_left_corner = (SCREEN_WIDTH / 2 - self.width / 2, SCREEN_HEIGHT / 2 - self.height / 2)

    self.selected_cell = None

    # add all the cells; where to change cell's values?
    for row in range(self.board_size):
      row_to_add = []
      matrix_row_to_add = []
      for col in range(0, self.board_size):
        row_to_add.append(Cell(int(pow(row * col, 0.5)), row, col, self.screen, self.top_left_corner))
        matrix_row_to_add.append(0)
      self.cells.append(row_to_add)
      self.matrix.append(matrix_row_to_add)

  def draw(self):
    for line in range(self.board_size + 1):
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (self.top_left_corner[0] + CELL_WIDTH * line, self.top_left_corner[1]),
            (self.top_left_corner[0] + CELL_WIDTH * line, self.top_left_corner[1] + self.height),
            6 if line % 3 == 0 else 3
        )
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (self.top_left_corner[0], self.top_left_corner[1] + CELL_HEIGHT * line),
            (self.top_left_corner[0] + self.width, self.top_left_corner[1] + CELL_HEIGHT * line),
            6 if line % 3 == 0 else 3
        )

    for i in range(len(self.cells)):
        for j in range(len(self.cells[i])):
            self.cells[i][j].draw()

  def select(self, row, col):
    if self.selected_cell is not None:
      self.selected_cell.selected = False
    self.selected_cell = self.cells[row][col]
    self.selected_cell.selected = True

  # Returns None if the click is outside the board, otherwise returns a tuple
  # of the form (x, y) with the column and row of the clicked cell
  def click(self, x, y):
    if x > self.top_left_corner[0] and x < self.top_left_corner[0] + self.width \
      and y > self.top_left_corner[1] and y < self.top_left_corner[1] + self.height:
        return int((x - self.top_left_corner[0]) // CELL_WIDTH), int((y - self.top_left_corner[1]) // CELL_HEIGHT)
    else:
      print("Click not on board!!!!!!")
      return None

  def clear(self):
    # TODO: how to differentiate between user-inputted values and
    # predetermined values?
    pass

  def sketch(self, value):
    if self.selected_cell is not None:
      self.selected_cell.set_sketched_value(value)
    else:
      print("Error: no cell selected!")

  def place_number(self, value):
    if self.selected_cell is None:
      print("Error: no cell selected!")
    else:
      self.selected_cell.set_cell_value(value)

  def reset_to_original(self):
    pass

  def is_full(self):
    for row in range(len(self.cells)):
      for col in range(len(self.cells[row])):
        cell = self.cells[row][col]
        if cell.value == 0:
          return False
    return True

  def update_board(self):
    for row in range(len(self.cells)):
      for col in range(len(self.cells[row])):
        self.matrix[row][col] = self.cells[row][col].value

  def find_empty(self):
    for row in range(len(self.cells)):
      for col in range(len(self.cells[row])):
        cell = self.cells[row][col]
        if cell.value == 0:
          return (cell.col, cell.row)
    print("No empty cells found!")

  def check_board(self):
    pass
