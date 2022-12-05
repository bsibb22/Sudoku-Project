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
    selection_font = pygame.font.Font(None, 80)

    screen.fill(BACKGROUND_COLOR)

    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    selection_surface = selection_font.render("Select Game Mode:", 0, LINE_COLOR)
    selection_rectangle = selection_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(selection_surface, selection_rectangle)

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center=(SCREEN_WIDTH // 2 - 250, SCREEN_WIDTH // 2 + 150))
    medium_rectangle = medium_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(SCREEN_WIDTH // 2 + 250, SCREEN_WIDTH // 2 + 150))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(
                        event.pos):  # depending on diffuculty selected the board will be generated differently
                    return "easy"
                elif medium_rectangle.collidepoint(event.pos):
                    return "medium"
                elif hard_rectangle.collidepoint(event.pos):
                    return "diffucult"

            pygame.display.update()


def draw_game_won(screen):
    end_title_font = pygame.font.Font(None, 100)  # font and background initailzations
    button_font = pygame.font.Font(None, 70)

    screen.fill(BACKGROUND_COLOR)

    title_surface = end_title_font.render("Game Over!", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    restart_text = button_font.render("Restart", 0, (255, 255, 255))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 + 150))

    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(
                        event.pos):
                    return

            pygame.display.update()


def draw_game_lost(screen):
    end_title_font = pygame.font.Font(None, 100)  # font and background initailzations
    button_font = pygame.font.Font(None, 70)

    screen.fill(BACKGROUND_COLOR)

    title_surface = end_title_font.render("Game Over:(", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 + 150))

    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(
                        event.pos):
                    pygame.quit()

            pygame.display.update()


#  v later scale based on difficulty
generator = SudokuGenerator(BOARD_SIZE, 10)
generator.board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, "easy", BOARD_SIZE)

if __name__ == "__main__":
    # area to initalize variables if needed
    winner_status = 0

    while True:
        screen.fill(BACKGROUND_COLOR)

        generator.board.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
