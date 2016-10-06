import pygame
from random import randint

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 127, 200)


size = [500, 500]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 10, True, False)

pygame.display.set_caption("Under Construction Shooter <3")

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)



#find out how to make a health bar

health = 100

#make display for stage
stage = 0


score = 0

x_coord = 250
y_coord = 450

x_speed = 0
y_speed = 0

sprites = [{"type": "player", "x_coord": x_coord, "y_coord": y_coord, "health": health, "x_width": 20, "y_length": 30, "color": blue}]
		
def spawnbasicenemies(amount):

	#still needs to be updates so enemies cant collide

	for i in range(amount):
		x = randint(50, 420)
		y = randint(50, 230)
	
		new_enemy = {"type": "basic_enemy", "x_coord": x, "y_coord": y, "x_width": 30, "y_length": 20, "health": 10, "color": pink}

		sprites.append(new_enemy)
		
def drawsprites(sprites):
	
	x = 0
	for i in sprites:
		pygame.draw.rect(screen, sprites[x]["color"], [sprites[x]["x_coord"], sprites[x]["y_coord"], sprites[x]["x_width"], sprites[x]["y_length"]])
		x += 1
		
#def movesprite(sprite):

#	#basic physics all objects have, move them by their speed
	
#	sprite["x"] += sprite["x_speed"]
#	sprite["y"] += sprite["y_speed"]
	
#	if sprite["type"] == "player":
		#cool player stuff here
		
#	elif sprite["type"] == "enemy_ship":
#		#cool enemy stuff here

#	elif sprite["type"] == "basic_enemy":
		#move cool stuff
		
#def detectcollisions(object_a, object_b):	


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
	
	text = font.render("Score", True, white)
	screen.blit(text, [0,0])

	text = font.render(str(score), True, white)
	screen.blit(text, [60, 0])
	
	text = font.render("Stage:", True, white)
	screen.blit(text, [420, 0])
	
	text = font.render(str(stage), True, white)
	screen.blit(text, [475, 0])
	
	drawsprites(sprites)
	pygame.display.flip()

	

	x_coord = x_coord + x_speed
	sprites[0]["x_coord"] = x_coord
	
	
	
	
	if stage == 0:
		spawnbasicenemies(5)
		
		stage = stage + 1
	


				
	if x_coord < 0:
		x_coord = 0
		
	elif x_coord + 20 > 500:
		x_coord = 500 - 20
		
	clock.tick(60)
	
pygame.quit()