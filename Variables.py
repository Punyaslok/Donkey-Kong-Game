import pygame, sys
from pygame.locals import *
import random
import time


pygame.init()

""" Stores Variables available across all modules """
floor_list = pygame.sprite.Group()
	
borders_list = pygame.sprite.Group()

princess_list = pygame.sprite.Group()




princess_image = "princess.png"
princess_x = 0
princess_y = 0
princess_height = 50
princess_width = 50


goldcoin_image = "goldcoin.png"
goldcoin_list = pygame.sprite.Group()
goldcoin_height = 40
goldcoin_width = 40



fireball_image = "fireball.png"
fireball_list = pygame.sprite.Group()
fireball_speed = 5
fireball_height = 40
fireball_width = 40
fireball_lower_limit = 0
fireball_upper_limit = 1000
fireball_divisor = 300





ladder_list = pygame.sprite.Group()
ladder_width = 75
ladder_image = "ladder.png"




scr_width = 1366
scr_height = 768

background_color = (0,171,255)

screen = pygame.display.set_mode((scr_width, scr_height),0,32)


floor_thickness = 15
floor_width = (scr_width*3)/4



mario_image = "mario.png"
mario_width = 40
mario_height = 40



donkey_image = "donkey.png"
donkey_width = 57
donkey_height = 47
donkey_speed = 4


border_thickness = 30
border_color = (97, 31, 107)

onscreen_textcolor = (255,0,0)
def message_to_screen(msg, color, inp_x, inp_y, size):
	font = pygame.font.SysFont( None, size )
	screen_text = font.render( msg, True, color )
	screen.blit(screen_text, [inp_x,inp_y])

def center_display(msg, color, size):
	font = pygame.font.Font(None, size)
	text = font.render(msg, 1, color)
	textpos = text.get_rect()
	textpos.centerx = screen.get_rect().centerx
	textpos.centery = screen.get_rect().centery
	screen.blit(text, textpos)

score_textcolor = (0,0,0)
def score_display(msg, color):
	font = pygame.font.Font(None, 40)
	text = font.render(msg, 1, color)
	textpos = text.get_rect()
	textpos.centerx = screen.get_rect().centerx
	textpos.y = scr_height - border_thickness + 2
	screen.blit(text, textpos)
