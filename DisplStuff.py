import pygame
from Clubs import *

pygame.init()

scrn = pygame.display.set_mode((0, 0))

def arrow():
    pygame.draw.rect(scrn, Red, (1600, 50, 100, 50))
    pygame.draw.polygon(scrn, Red, ((1700, 0), (1700, 150), (1750, 75)))
    pygame.display.update()

def msgbox(text, pos, size):
    msg = pygame.font.SysFont('Comic Sans M',  size).render(text, True, White)
    scrn.blit(msg, pos)

def centerbox(text, pos, size):
    msg = pygame.font.SysFont('Comic Sans M',  size).render(text, True, White)
    msgRect = msg.get_rect(center = pos)
    scrn.blit(msg, msgRect)