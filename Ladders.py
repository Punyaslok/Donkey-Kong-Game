import pygame, sys 
from pygame.locals import *
import random
import time

from Variables import *

pygame.init()



class Ladder(pygame.sprite.Sprite):
	def __init__( self , image_source, inp_x, inp_y, inp_height, inp_width ):
		pygame.sprite.Sprite.__init__(self)
		self.width = inp_width
		self.height = inp_height
		self.x = inp_x
		self.y = inp_y
		self.img_cursor = pygame.image.load(image_source).convert_alpha()
		self.img_cursor = pygame.transform.scale(self.img_cursor,(self.width,self.height))
		self.rect = self.img_cursor.get_rect()
		self.rect.x = inp_x
		self.rect.y = inp_y
	def draw(self):
		screen.blit(self.img_cursor,(self.x, self.y))


def generate_ladders(): 	#	Displays/Creates Ladders              # lev = difficulty level
	if not ladder_list:
		extension = 3	#	by how much ladder will protude from surface
		temp_height = ((scr_height - (2*border_thickness))/(len(floor_list)-2)) + extension
#		print len(floor_list)
		for i in floor_list:
			if i.width > i.thickness :
				temp_x = random.randint(scr_width - border_thickness - floor_width, scr_width - border_thickness - (scr_width - floor_width) - ladder_width - 10)
				temp_y = i.y - extension
				if i.alignment == 1 :
#				temp_x = random.randint(border_thickness+20, i.width - ladder_width - 20)
					temp_ladder = Ladder( ladder_image, temp_x, temp_y, temp_height, ladder_width )
				elif i.alignment == 0 :
#				temp_x = random.randint(scr_width - border_thickness - i.width + 20, scr_width - border_thickness - ladder_width - 20)
					temp_ladder = Ladder( ladder_image, temp_x, temp_y, temp_height, ladder_width )
				elif i.alignment == -1 :
					temp_x = random.randint(i.x + 10, i.x + i.width -10)
					temp_ladder = Ladder( ladder_image, temp_x, temp_y, ((temp_height)/2) + floor_thickness, ladder_width )

				ladder_list.add(temp_ladder)
		for i in ladder_list :
			temp_floor_list = pygame.sprite.spritecollide(i,floor_list,True)
			for j in temp_floor_list :
				j.split_floor(i.rect.left, i.rect.right)

	for i in ladder_list :
		i.draw()
	return
