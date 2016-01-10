import pygame, sys 
from pygame.locals import *
import random
import time

from Variables import *

pygame.init()

screen = pygame.display.set_mode((scr_width, scr_height),0,32)



class Borders(pygame.sprite.Sprite):
	def __init__( self , inp_x, inp_y, inp_thick, inp_width ):
		pygame.sprite.Sprite.__init__(self)
		self.width = inp_width		# Border Width
		self.thickness = inp_thick	# Border Thickness
		self.x = inp_x			# X and Y coordinates of border block
		self.y = inp_y
		self.image = pygame.Surface([inp_width, inp_thick])
		self.image.fill(border_color)
		self.rect = self.image.get_rect()
		self.rect.y = inp_y
		self.rect.x = inp_x

def generate_borders():		# Generates 4 Borders around the screen
	if not borders_list :
		temp_border1 = Borders(0, 0, border_thickness, scr_width )
		temp_border2 = Borders(0, 0, scr_height, border_thickness )
		temp_border3 = Borders(0, scr_height - border_thickness, border_thickness, scr_width )
		temp_border4 = Borders(scr_width - border_thickness, 0, scr_height, border_thickness )
		borders_list.add(temp_border1)
		borders_list.add(temp_border2)
		borders_list.add(temp_border3)
		borders_list.add(temp_border4)
	borders_list.draw(screen)
	return
