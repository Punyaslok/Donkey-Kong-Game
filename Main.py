import pygame, sys
from pygame.locals import *
import random
import time


from Variables import *
from Person_Class import *
from Borders import *
from Floors import *
from Ladders import *
from Goldcoin import *
from Fireball import *

pygame.init()

screen = pygame.display.set_mode([scr_width, scr_height],pygame.FULLSCREEN )

""" Frames per Second """
clock = pygame.time.Clock()
FPS = 60


def gameLoop(difficulty_level, score):

	player_obj = Player (mario_image, mario_width, mario_height, border_thickness + 5, scr_height - border_thickness-mario_height - 5)
	

	donkey_obj_list = pygame.sprite.Group()		# Multiple donkeys may be generated according to level

	for i in range(difficulty_level):		# Reset Donkeys
		donkey_obj_list.add (Donkey ( donkey_image, donkey_width, donkey_height, border_thickness + 5, 90 ) )
	
		
	if princess_list :				# Reset princess
		princess_list.empty()

	if floor_list :					# Reset Floors
		floor_list.empty()
	generate_floors(1)

	if goldcoin_list :				# Reset Goldcoins
		goldcoin_list.empty()
	generate_goldcoins()

	if fireball_list :				# Reset fireballs
		fireball_list.empty()
	generate_goldcoins()

	if ladder_list :				# Reset Ladders
		ladder_list.empty()
	generate_goldcoins()

	player_obj.score = 0				# Reset Player Attributes
	player_obj.rect.x = border_thickness + 5 
	player_obj.rect.y = scr_height - border_thickness-mario_height - 5

	gameExit = False				# Game Exit Flag. Closes the game
	gameOver = False				# New game flag

	while not gameExit :
		while gameOver == True :
			screen.fill((255,255,255))
			center_display("Game Over. Press C to play again, Q to Quit.",(0,255,0),80)
			pygame.display.update()
	
			for event in pygame.event.get():
				if event.type == KEYDOWN :
					if event.key == K_q:
						gameExit = True
						gameOver = False
						pygame.quit()	# the following 2 lines added to prevent remaking of screen before game exit
						sys.exit()
					elif event.key == K_c:
						gameLoop(1, 0)

		for event in pygame.event.get():
			if event.type == QUIT :
				gameExit = True	
#			player_obj.vel_x = 0
#			player_obj.vel_y = 0
			if event.type == KEYDOWN:
				if event.key == K_a :
					player_obj.vel_x = -6
				elif event.key == K_d :
					player_obj.vel_x = 6
				elif event.key == K_w and player_obj.ladder_collision() != 0 :
					 player_obj.vel_y = -3
				elif event.key == K_s and player_obj.ladder_collision() != 0 :
					 player_obj.vel_y = 3
					 player_obj.keydown_flag = True
				elif event.key == K_SPACE :
					 player_obj.jump()
			if event.type == KEYUP:
				if event.key == K_q:
					gameExit = True
				elif event.key == K_a:
					player_obj.vel_x = 0
				elif event.key == K_d:
					player_obj.vel_x = 0
				elif event.key == K_w:
					player_obj.vel_y = 0
				elif event.key == K_s:
					player_obj.vel_y = 0
					player_obj.keydown_flag = False

		screen.fill(background_color)
		generate_floors(1)
		generate_ladders()
		generate_borders()
		
		
		player_obj.move_horizontally(player_obj.vel_x)
		player_obj.gravity()
		player_obj.move_vertically(player_obj.vel_y)
		
#		print str(player_obj.rect.x) + ' ' + str(player_obj.rect.y)
		for i in donkey_obj_list :
			generate_fireball(i.rect.right, i.rect.bottom - fireball_height - 1)
		for i in donkey_obj_list :	# Update donkey positions
			i.update()


		display_goldcoins()
		player_obj.check_coin_collisions()	# Check collisions with coins
		
		player_obj.check_fireball_collisions()	# Check collisions with fireballs
		player_obj.draw()
		for i in donkey_obj_list :		# Draw all donkeys
			i.draw()
	
		if pygame.sprite.spritecollide(player_obj, princess_list, False) :	# When player collides with princess
			final_message = 'Score : ' + str(score)# + ' Lives : ' + str(player_obj.lives)
			screen.fill((0,0,0))
			center_display(score_message, (255,255,255), 80)
			pygame.display.update()
			time.sleep(3)
			score += player_obj.score
			difficulty_level += 1
			gameLoop(difficulty_level, score)

#		print princess_list
		draw_princess()
		

		score_message = 'Score : ' + str(player_obj.score) + '      Lives : ' + str(player_obj.lives) + '      Level : ' + str(difficulty_level)		# Display Score
		score_display(score_message, score_textcolor)

		if pygame.sprite.spritecollide(player_obj, donkey_obj_list, False) or player_obj.lives == 0 :
			score += player_obj.score
			gameOver = True


		clock.tick(FPS)		# Control FPS
	
		pygame.display.update()

	pygame.quit()
	sys.exit()

if __name__ == "__main__":	# cant be run from another file
	gameLoop(1, 0)
