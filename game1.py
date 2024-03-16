import pygame
import sys
import random


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TLN Game")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 102, 0)


all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()
thorns = pygame.sprite.Group()
moving_platforms = pygame.sprite.Group()  # Add this line


gravity = 0.5
player_speed = 4
player_jump = -13
level_checker = 1
required_lvl1 = 5
required_lvl2 = 7


bg_img = pygame.image.load("bck.png").convert()
player_img = pygame.image.load("player.png").convert_alpha()
coin_img = pygame.image.load("coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (50, 50))
thorn_img = pygame.image.load("thorn.png").convert_alpha()
thorn_img = pygame.transform.scale(thorn_img, (50, 50))


font = pygame.font.Font(None, 36)

#Not decided yet what ost I want to be in my game
pygame.mixer.music.load('ost.mp3')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)
