# author: Nikola Zubic

import pygame
import characters_classes


def game_text(game_display, text_input, x, y, size=17, color=(255, 255, 255)):
    text = str(text_input)

    font = pygame.font.SysFont('Chilanka', size)

    text = font.render(text, True, color)
    game_display.blit(text, (x, y))


def help_menu_text(game_display, text_input, x, y, size=17, color=(255, 255, 255)):
    text = str(text_input)

    font = pygame.font.SysFont('Chilanka', size, bold=True)

    text = font.render(text, True, color)
    game_display.blit(text, (x, y))


def health_bar(game_display, player):
    pygame.draw.rect(game_display, (0, 0, 0), (10, 12, 100, 20))
    if player.health > 0:
        pygame.draw.rect(game_display, (77, 255, 0), (10, 12, player.health, 20))


def score(game_display, fps, total_frames):
    game_text(game_display, int(total_frames / fps), 990, 10, 35)
    game_text(game_display, characters_classes.Enemy.score, 990, 50, 35)
    game_text(game_display, "Score:", 860, 50, 35)
    game_text(game_display, "Timer:", 860, 10, 35)
