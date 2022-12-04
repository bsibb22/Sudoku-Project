from constants import *
import pygame

class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.sketched_value = 0

  def set_cell_value(self, value):
    self.value = value

  def Set_sketched_value(self, value):
    self.sketched_value = value
    
  def draw(self):
    if self.value != 0:
      return self.value
    else:
      return None