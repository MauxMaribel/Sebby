import pygame
from random import randint

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Under Construction Shooter <3")

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

#needs to be adjusted into sprite list
enemies = []

level = 0

sprites = []
		
def spawnenemies(amount):

	#still needs to be updates so enemies cant collide

	for i in range(amount):
		x = randint(50, 420)
		y = randint(50, 230)
	
		new_enemy = [x, y, 30, 20]
		enemies.append(new_enemy)
		
		
def drawenemies(enemies):
	#needs to become drawsprites
	
	for i in enemies:
		pygame.draw.rect(screen, red, i)
		
#def movesprite(sprite):

#	#basic physics all objects have, move them by their speed
	
#	sprite["x"] += sprite["x_speed"]
#	sprite["y"] += sprite["y_speed"]
	
#	if sprite["type"] == "player":
		#cool player stuff here
		
#	elif sprite["type"] == "enemy_ship":
#		#cool enemy stuff here
		
	

	
		

	
	

x_coord = 250
y_coord = 450

x_speed = 0
y_speed = 0

while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				x_speed = -3
			
			elif event.key == pygame.K_d:
				x_speed = 3
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				x_speed = 0
				
	player = [x_coord, y_coord, 20, 30]
	
	score = 0
				
	screen.fill(black)
	pygame.draw.rect(screen, blue, [x_coord, y_coord, 20, 30])
	drawenemies(enemies)
	pygame.display.flip()

	

	x_coord = x_coord + x_speed
	
	
	
	if level == 0:
		spawnenemies(5)
		
		level = level + 1
	


				
	if x_coord < 0:
		x_coord = 0
		
	elif x_coord + 20 > 500:
		x_coord = 500 - 20
		
	clock.tick(60)
	
pygame.quit()