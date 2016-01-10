import pygame, sys 
from pygame.locals import *
import random
import time

from Variables import *
from Person_Class import *

pygame.init()

#screen = pygame.display.set_mode((scr_width, scr_height),0,32)



class Floor(pygame.sprite.Sprite):
	def __init__( self , inp_x, inp_y, inp_thick, inp_width , align):
		pygame.sprite.Sprite.__init__(self)
		self.width = inp_width		#	Floor width
		self.thickness = inp_thick	#	Floor Thickness
		self.x = inp_x
		self.y = inp_y
		self.alignment = align	# alignment = 1 for left , 0 for right
		self.image = pygame.Surface([inp_width, inp_thick])
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.y = inp_y
		self.rect.x = inp_x
	def split_floor (self, input_x1, input_x2) :	# Split the floor after ladders are added
		if abs ( self.rect.left - input_x1 ) >= 3 :
			floor_list.add(Floor(self.rect.left, self.rect.y, self.thickness, input_x1 - self.rect.left, -1))
		if self.rect.right - input_x2 >= 3 :
			floor_list.add(Floor(input_x2, self.rect.y, self.thickness, self.rect.right - input_x2, -1))
		return


def generate_floors(lev):               # lev = difficulty level	#	Creates (for first time) and displays floors
	if not floor_list:
		no_of_floors = lev + 5 
		for i in range( 1, no_of_floors  ):  
#			print i
			align = i%2 
			temp_y = ((scr_height - (2*border_thickness))*i)/no_of_floors + 2*floor_thickness
			if align == 1 :
				temp_floor = Floor( border_thickness, temp_y, floor_thickness, floor_width, align)
			elif align == 0 : 
				temp_floor = Floor(scr_width - border_thickness - floor_width, temp_y, floor_thickness, floor_width, align)
#			print temp_floor
			floor_list.add(temp_floor)

		""" Adding Princess Platform Base """
		princess_floor_x = random.randint( border_thickness + donkey_width + 60, (floor_width - (scr_width/3) ))
		princess_floor_y = (((scr_height - (2*border_thickness)))/no_of_floors)/2 + floor_thickness
		princess_floor = Floor( princess_floor_x, princess_floor_y, floor_thickness, scr_width/3, -1 )	#	Princess Floor (has alignment -1)
		floor_list.add(princess_floor)
		
		""" Adding Princess Platform Boundaries """
		temp_p_floor_left = Floor( princess_floor.rect.left, border_thickness, princess_floor.rect.top - border_thickness, floor_thickness, -1 )
		princess_x = princess_floor.rect.left + border_thickness
		princess_y = princess_floor.rect.top - princess_height
		princess_list.add( (Princess(princess_image, princess_width, princess_height, princess_x, princess_y)) )


		floor_list.add(temp_p_floor_left)
		temp_p_floor_right = Floor( princess_floor.rect.right - floor_thickness, border_thickness, princess_floor.rect.top - border_thickness, floor_thickness, -1 )
		floor_list.add(temp_p_floor_right)
#	print floor_list
	floor_list.draw(screen)
	return
