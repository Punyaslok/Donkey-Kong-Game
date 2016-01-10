import pygame, sys
from pygame.locals import *
import random
import time

from Variables import *

pygame.init()

class Goldcoin(pygame.sprite.Sprite):
	def __init__(self, image_source, w, h, inp_x, inp_y):
		self.x = inp_x
		self.y = inp_y
		self.width = w
		self.height = h
		pygame.sprite.Sprite.__init__(self)
		self.img_cursor = pygame.image.load(image_source).convert_alpha()
		self.img_cursor = pygame.transform.scale(self.img_cursor,(self.width,self.height))
	  	self.rect = self.img_cursor.get_rect()
	  	self.rect.x = inp_x
	  	self.rect.y = inp_y

	def draw(self):		# Custom Draw function to draw single sprite
		screen.blit(self.img_cursor, (self.rect.x, self.rect.y))


def generate_goldcoins():		# Displays Goldcoins (in the first call, the function creates the list and then displays them)
	if not goldcoin_list:
		for i in floor_list :
			if i.width > i.thickness and i.width > scr_height/2 :	# dont consider princess floors
				number = random.randint(5, 10)
				for j in range(number) :
					temp_x = random.randint(border_thickness + 5, scr_width - border_thickness - goldcoin_width - 5)
					temp_y =  ( i.rect.top - goldcoin_height - 2 )
					temp_coin = Goldcoin(goldcoin_image, goldcoin_width, goldcoin_height, temp_x, temp_y)
					pygame.sprite.spritecollide(temp_coin, goldcoin_list, True)	# remove colliding coins
					goldcoin_list.add(temp_coin)
	return

def display_goldcoins():	# Draw all coins
	for i in goldcoin_list :
		i.draw()
	return
