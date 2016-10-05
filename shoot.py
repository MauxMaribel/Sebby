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

enemies = []

class Enemy(object):

	#So needs more work and research before being a thing
	
	def __init__(self):
	
		x = randint(50, 220)
		y = randint(50, 430)
	
		pygame.draw.rect(screen, red, [x, y, 30, 20])
		
		pygame.screen.flip()
		
def spawnenemies(amount):

	#needs some code here
	
	return True

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
	pygame.display.flip()
	
	x_coord = x_coord + x_speed
	
	

				
	if x_coord < 0:
		x_coord = 0
		
	elif x_coord + 20 > 500:
		x_coord = 500 - 20
		
	clock.tick(60)
	
pygame.quit()