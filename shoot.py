import pygame
from random import randint

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 127, 200)
purple = (200, 100, 230)
orange = (255, 127, 0)
l_blue = (0, 240, 255)
yellow = (255, 255, 0)

colors = [red, green, blue, pink, purple, l_blue, orange, yellow, white]




size = [500, 500]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 15, True, False)

pygame.display.set_caption("Under Construction Shooter <3")

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)





#find out how to make a health bar

health = 100


stage = 0

#bonus for accurate shots. Later show combo on screen
combo = 0

score = 0

x_coord = 250
y_coord = 450

x_speed = 0
y_speed = 0

sprites = [{"type": "player", "x_coord": 250, "y_coord": 450, "health": health, "x_width": 20, "y_length": 30, "x_speed": 0, "y_speed": 0, "color": blue}]


def DetectCollisions(rect_a, rect_b):

	#rect_a[0] = plat_xcoord
	#rect_a[1] = plat_ycood
	#rect_a[2] = plat_xwidth
	#rect_a[3] = plat_yheight
	
	#rect_b[0] = player_xcoord
	#rect_b[1] = player_ycoord
	#rect_b[2] = player_xwidth
	#rect_b[3] = player_yheight
	#Boolean Logic: OR auto true unless both False, AND auto false unless both True
	
	#x_apart = plat_xcoord >= player_xcoord + player_xwidth or player_xcoord >= plat_xcoord + plat_xwidth
	#y_apart = plat_ycoord >= player_ycoord + player_yheight or player_ycoord >= plat_ycoord + plat_yheight

	x_apart = rect_a[0] >= rect_b[0] + rect_b[2] or rect_b[0] >= rect_a[0] + rect_a[2]
	y_apart = rect_a[1] >= rect_b[1] + rect_b[3] or rect_b[1] >= rect_a[1] + rect_a[3]
	
	return x_apart == False and y_apart == False
	
def enemydeath(enemy):
	
	x = enemy["x_coord"]
	y = enemy["y_coord"]
	color = colors[randint(0, 8)]
	color2 = colors[randint(0, 8)]

	i = 50
	while i > 0:
		x_speed = randint(-3, 3)
		y_speed = randint(-3, 3)
		part = {"type": "particle", "x_coord": x, "y_coord": y, "x_speed": x_speed, "y_speed": y_speed, "y_length": 2, "x_width": 2, "time": 9, "health": 2, "color": color, "color2": color2}
		sprites.append(part)
		i -= 1


def NextStage(level):

	global stage

	#insert some text or animations for stage increase
	m = 0
	new_stage = True
	for i in sprites:
		if sprites[m]["type"] == "basic_enemy":
			new_stage = False
		m += 1
			
	if new_stage == True:
		spawnbasicenemies(level + 2)
		stage += 1
	
	
def EnemyCollision(new_enemy):

	z = 0

	rect_a = [new_enemy["x_coord"],new_enemy["y_coord"],new_enemy["x_width"],new_enemy["y_length"]]


	
	for item in sprites:
		rect_b = [sprites[z]["x_coord"],sprites[z]["y_coord"],sprites[z]["x_width"],sprites[z]["y_length"]]
		if DetectCollisions(rect_a, rect_b) == True and sprites[z]["type"] != "p_bullet":
			return z
		else:
			z += 1
			
	return False

		
def spawnbasicenemies(amount):

	
	
	i = amount
	
	while i > 0:

		x = randint(50, 420)
		y = randint(50, 230)
		color = colors[randint(0, 8)]
	
		new_enemy = {"type": "basic_enemy", "x_coord": x, "y_coord": y, "x_width": 30, "y_length": 20, "x_speed": 0, "y_speed": 0, "health": 10, "score": 100, "color": color}

		if EnemyCollision(new_enemy) == False:

			sprites.append(new_enemy)
			i -= 1

def firebullet(amount):

	global combo


	x = sprites[0]["x_coord"] + 10
	y = sprites[0]["y_coord"] - 6
	color = colors[randint(0, 8)]
	
	new_bullet = {"type": "p_bullet", "x_coord": x, "y_coord": y, "x_width": 2, "y_length": 6, "y_speed": -10, "x_speed": 0, "damage": 5, "health": 1, "color": color}
	sprites.append(new_bullet)
	
	combo += 1
		
def drawsprites(sprites):
	
	x = 0
	for i in sprites:
		pygame.draw.rect(screen, sprites[x]["color"], [sprites[x]["x_coord"], sprites[x]["y_coord"], sprites[x]["x_width"], sprites[x]["y_length"]])
		x += 1
		
def movesprite(sprites):

	global score
	global combo

	#basic physics all objects have, move them by their speed
	i = 0
	while i < len(sprites):
		sprites[i]["x_coord"] += sprites[i]["x_speed"]
		sprites[i]["y_coord"] += sprites[i]["y_speed"]
	
		if sprites[i]["type"] == "p_bullet":
			if sprites[i]["y_coord"] < 0:
				sprites.remove(sprites[i])
				combo = 0
			elif EnemyCollision(sprites[i]) != False:
				enemy = EnemyCollision(sprites[i])
				if sprites[enemy]["type"] != "particle":
					sprites[enemy]["health"] = sprites[enemy]["health"] - sprites[i]["damage"]
					sprites.remove(sprites[i])

			
		
		elif sprites[i]["health"] <= 0:
			if sprites[i]["type"] != "player":
				score += sprites[i]["score"] * combo
				enemydeath(sprites[i])
				sprites.remove(sprites[i])
				
		elif sprites[i]["type"] == "particle":
			if sprites[i]["time"] == 2:
				sprites[i]["color"] = sprites[i]["color2"]
			
			sprites[i]["time"] -= 1	
			
			if sprites[i]["time"] <= 0:
				sprites.remove(sprites[i])

		
		elif sprites[i]["x_coord"] < 0:
			sprites[i]["x_coord"] = 0
		
		elif sprites[i]["x_coord"] + 20 > 500:
			sprites[i]["x_coord"] = 500 - 20
		i += 1
		
	



while not done:

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				sprites[0]["x_speed"] = -5
			
			elif event.key == pygame.K_d:
				sprites[0]["x_speed"] = 5
				
			elif event.key == pygame.K_SPACE:
				firebullet(1)
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				sprites[0]["x_speed"] = 0
				
	
	
	
	
	movesprite(sprites)
	
	
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

	
	
	
	
	NextStage(stage)
	
	


		
	clock.tick(60)
	
pygame.quit()