import pygame, sys
from pygame.locals import *
import random
import time

from Variables import *

pygame.init()

class Fireball(pygame.sprite.Sprite):
	def __init__(self, image_source, w, h, inp_x, inp_y):
#		self.jump_flag = False
		self.x = inp_x		
		self.y = inp_y
		self.vel_x = 0	# Velocities
		self.vel_y = 0
		self.width = w
		self.height = h
		pygame.sprite.Sprite.__init__(self)
		self.img_cursor = pygame.image.load(image_source).convert_alpha()
		self.img_cursor = pygame.transform.scale(self.img_cursor,(self.width,self.height))
	  	self.rect = self.img_cursor.get_rect()
	  	self.rect.x = inp_x
	  	self.rect.y = inp_y

	def ladder_collision(self):		#	Checks if a fireball is colliding with a ladder
		temp_list = pygame.sprite.spritecollide(self,ladder_list, False)
		if not temp_list :
			return 0
		return 1
		
	def floor_collision(self):	# Checks if  a fireball is colliding with the floor
		temp_list = pygame.sprite.spritecollide(self,floor_list, False)
		for i in temp_list :
			return i
		return 0

	def border_collision(self):	# Checks if a fireball is colliding with the borders
		temp_list = pygame.sprite.spritecollide(self,borders_list, False)
		for i in temp_list :
			return i
		return 0

	def move_vertically(self, val):		# Vertical Movmement
		if self.ladder_collision() == 1 :	# Decides whether to go down the ladder
#			print 'val = ' + str(val)
			t = random.randint(0,1)
			if (t == 1) :
				self.rect.y += 10
		if val == 0 :
			return
		self.rect.y += val
		temp_border = self.border_collision()
		if temp_border != 0:
			if val > 0 :
				self.rect.bottom = temp_border.rect.top
				self.jump_flag = False
			elif val < 0 :
				self.rect.top = temp_border.rect.bottom
			self.vel_y = 0
			return
		temp_floor = self.floor_collision()
		if temp_floor != 0 :
			if val > 0 :
				self.rect.bottom = temp_floor.rect.top
				self.jump_flag = False
			elif val < 0 :
#				if self.ladder_collision() == 1 :
#					self.rect.bottom = temp_floor.rect.top
#				else:
					self.rect.top = temp_floor.rect.bottom
			rand_x_vel = random.randint(0,1)
			if rand_x_vel == 0 and self.vel_y > 5:
#				print self.vel_y
				self.vel_x = self.vel_x * (-1)
			self.vel_y = 0
		return

	def jump(self) :	# Simulates jump
		if self.jump_flag == True:
			return
		else:
			self.jump_flag = True
			self.standing_flag = False
			self.vel_y = -10
		return
	
	def gravity(self):	# Provides gravity effect
#		if self.ladder_collision() == 1 :
#			print "ladder"
#			return
#		if self.vel_y == 0 :
#			return
#		else :
		self.move_vertically(self.vel_y)
		self.vel_y += 0.35
		return


	def draw(self):		# Custom Draw function to draw single sprite
		screen.blit(self.img_cursor, (self.rect.x, self.rect.y))

	def update(self):	#	Finds next possible position of fireball
#		print fireball_speed
		if self.vel_x == 0 :
			self.vel_x = fireball_speed
		elif self.vel_x > 0 :
			if self.rect.right >= scr_width - border_thickness - 10:
				self.rect.right = scr_width - border_thickness - 1
				self.vel_x = self.vel_x * (-1)
		elif self.vel_x < 0 :
#			print 'bottom = ' + str(self.rect.bottom) + ' floor = ' + str(scr_height - border_thickness - 30)
			if self.rect.left < border_thickness + 10 and self.rect.bottom > scr_height - border_thickness - 30 :
				self.remove(fireball_list)
#				print "satisfied"
				return
			if self.rect.left <= border_thickness + 5 :
				self.vel_x = self.vel_x * (-1)
		self.rect.x += self.vel_x
		return

def generate_fireball(donk_x, donk_y):		# May Generate a fireball at the donkey's location
	temp_rand = random.randint(fireball_lower_limit, fireball_upper_limit)
	if temp_rand % fireball_divisor == 0 :
		fireball_list.add(Fireball(fireball_image, fireball_width, fireball_height, donk_x, donk_y ))
	for i in fireball_list :
		i.update()
		i.gravity()
		i.draw()
	return
