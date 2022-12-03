import pygame
from constants import *
from sudoku_generator import SudokuGenerator

pygame.init()
pygame.display.set_caption("Sudoku Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#                                        v later scale based on difficulty
generator = SudokuGenerator(BOARD_SIZE, 10)
generator.board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, "easy", BOARD_SIZE)

if __name__ == "__main__":
  while True:
    generator.board.draw()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    pygame.display.update()