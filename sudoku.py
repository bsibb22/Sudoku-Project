import pygame
from constants import *
from sudoku_generator import SudokuGenerator
from board import Board
 
pygame.init()
pygame.display.set_caption("Sudoku Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)  # font and background initailzations
    button_font = pygame.font.Font(None, 70)
    selection_font = pygame.font.Font(None,80)
    
    screen.fill(BACKGROUND_COLOR)

    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    selection_surface = selection_font.render("Select Game Mode:",0,LINE_COLOR)
    selection_rectangle = selection_surface.get_rect(
        center=(SCREEN_WIDTH //2, SCREEN_HEIGHT // 2 -20))
    screen.blit(selection_surface,selection_rectangle)

    easy_text = button_font.render("Easy",0,(255,255,255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0]+20,easy_text.get_size()[1]+20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0]+20,hard_text.get_size()[1]+20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text,(10,10))

    easy_rectangle = easy_surface.get_rect(
        center= (SCREEN_WIDTH //2 -250, SCREEN_WIDTH//2 +150))
    medium_rectangle = medium_surface.get_rect(
        center= (SCREEN_WIDTH //2 , SCREEN_WIDTH//2 +150))
    hard_rectangle = hard_surface.get_rect(
        center= (SCREEN_WIDTH //2 +250, SCREEN_WIDTH//2 +150))

    screen.blit(easy_surface,easy_rectangle)
    screen.blit(medium_surface,medium_rectangle)
    screen.blit(hard_surface,hard_rectangle)

#                                        v later scale based on difficulty
generator = SudokuGenerator(BOARD_SIZE, 10)
generator.board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, "easy", BOARD_SIZE)


if __name__ == "__main__":
#area to initalize variables if needed

  
  while True:
    generator.board.draw()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    pygame.display.update()