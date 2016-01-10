import pygame, sys
from pygame.locals import *
import random
import time

from Variables import *

pygame.init()

class Person(pygame.sprite.Sprite):
	def __init__(self, image_source, w, h, inp_x, inp_y):
		self.keydown_flag =  False	# stores if any key is pressed or not. Used to prevent player from sliding down the stairs automatically
		self.jump_flag = False	# Flag to indicate whether player is jumping
		self.standing_flag = True	# Flag for standing
		self.x = inp_x
		self.y = inp_y
		self.vel_x = 0		# Velocities in x and y directions
		self.vel_y = 0
		self.width = w
		self.height = h
		pygame.sprite.Sprite.__init__(self)
		self.img_cursor = pygame.image.load(image_source).convert_alpha()
		self.img_cursor = pygame.transform.scale(self.img_cursor,(self.width,self.height))
	  	self.rect = self.img_cursor.get_rect()
	  	self.rect.x = inp_x
	  	self.rect.y = inp_y

	def ladder_collision(self):	# Detects collision with Ladder
		temp_list = pygame.sprite.spritecollide(self,ladder_list, False)
		if not temp_list :
			return 0
		return temp_list
		
	def floor_collision(self):	# Detects collision with Floor
		temp_list = pygame.sprite.spritecollide(self,floor_list, False)
		for i in temp_list :
			return i
		return 0

	def border_collision(self):	# Detects collision with Borders
		temp_list = pygame.sprite.spritecollide(self,borders_list, False)
		for i in temp_list :
			return i
		return 0

	def move_horizontally(self, val):
		if val == 0 :
			return
		self.rect.x += val
		temp_border = self.border_collision()
		if temp_border != 0 :
			if val > 0 :
				self.rect.right = temp_border.rect.left
			elif val < 0 :
				self.rect.left = temp_border.rect.right
			self.vel_x = 0
			return

		temp_floor = self.floor_collision()
		if temp_floor != 0:
			if val > 0 :
				self.rect.right = temp_floor.rect.left
			elif val < 0 :
				self.rect.left = temp_floor.rect.right
			self.vel_x = 0
			return
		return
								
	def move_vertically(self, val):
#		if val < 0 :
#			print "negative"
#		print self.keydown_flag
		t = self.ladder_collision()
		if t != 0 :
			for i in t :
				if self.keydown_flag == False and val > 0 :
#					self.rect.bottom = i.rect.y
					self.vel_y = 0
					val = 0
			self.rect.y += val
#			print 'val = ' + str(val)
#			if keydown_flag == False:
#				for i in t :
#					self.rect.bottom = i.rect.top
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
			self.vel_y = 0
		return

	def jump(self) :
		if self.jump_flag == True:
			return
		else:
			self.jump_flag = True
			self.standing_flag = False
			self.vel_y = -8
		return
	
	def gravity(self):
		if self.ladder_collision() != 0 :
			return
#		if self.vel_y == 0 :
#			return
#		else :
		self.move_vertically(self.vel_y)
		self.vel_y += 0.35
		return


	def draw(self):		# Custom Draw function to draw single sprite
		screen.blit(self.img_cursor, (self.rect.x, self.rect.y))


class Player(Person):
	def __init__(self, image_source, w, h, inp_x, inp_y):
		self.score = 0
		self. lives = 5
		Person.__init__(self, image_source, w, h, inp_x, inp_y)

	def check_coin_collisions(self):	# Detects collision with Coins
		coin_hit_list = pygame.sprite.spritecollide(self, goldcoin_list, True)
		for temp_coin in coin_hit_list:
			self.score += 5
		return

	def check_fireball_collisions(self):	# Detects collision with Fireballs
		fireball_hit_list = pygame.sprite.spritecollide(self, fireball_list, True)
		if not fireball_hit_list :
			return
		self.score -= 25
		self.lives -= 1
		if self.score < 0 :
			self.score = 0
		self.rect.left = border_thickness + 1
		self.rect.bottom = scr_height - border_thickness - 1
		center_display('Score : ' + str(self.score) +  ' Lives Remaining : ' + str(self.lives),(0,0,0), 100)
		pygame.display.update()
		time.sleep(2)
		return

class Donkey(Person):
	def __init__(self, image_source, w, h, inp_x, inp_y):
		Person.__init__(self, image_source, w, h, inp_x, inp_y)
	
	def update(self):
#		print 'Donkey x = ' + str(self.rect.x) + ' y = ' + str(self.rect.y)
		self.gravity()
		if self.vel_x == 0 :
			self.vel_x = donkey_speed

		elif self.vel_x > 0 :
			if self.rect.right >= border_thickness + floor_width :
				self.rect.right = border_thickness + floor_width
				self.vel_x = (-1)*donkey_speed
				return

		elif self.vel_x < 0 :
			if self.rect.left <= border_thickness + 10:
				self.rect.x = border_thickness + 1
				self.vel_x = donkey_speed
		self.rect.x += self.vel_x
		t = random.randint(0, 50)
		if t % 27 == 0 :
			self.vel_x *= (-1)
		return

class Princess(Person):
	def __init__(self, image_source, w, h, inp_x, inp_y):
		Person.__init__(self, image_source, w, h, inp_x, inp_y)

def draw_princess():		# Draws Princess
	for i in princess_list:
		i.draw()
	return
