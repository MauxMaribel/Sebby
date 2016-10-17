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
bcolors = [white, pink, yellow]



size = [500, 500]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 15, True, False)

button_font = pygame.font.SysFont('Calibri', 25, True, False)

pygame.display.set_caption("Under Construction Shooter <3")

#This is a Button class. You can create buttons using
#Button() to create a new button object.
#
#Example:
#mybutton = Button()
#mybutton.text = 'Play Game'
#mybutton.color = pink
#mybutton.text_color = black
class Button:
	x = 100
	y = 100
	w = 120
	h = 80

	#The text on the button. Change this after creating
	#a button to set what you want the text to be.
	text = "test"
	color = blue
	color_mouseover = red
	text_color = white

	#records if the mouse button was pressed on the previous
	#frame so we can tell if the player has just pressed the
	#mouse button.
	mouse_clicked_last_frame = False

	has_been_clicked = False

	#When the player clicks the mouse button this function will
	#return true the next time you call it.
	def clicked(self):
		result = self.has_been_clicked
		self.has_been_clicked = False
		return result

	#tells us if the mouse is currently inside the button.
	def is_mouseover(self):
		mouse_x = pygame.mouse.get_pos()[0]
		mouse_y = pygame.mouse.get_pos()[1]

		return mouse_x > self.x and mouse_x < self.x+self.w and mouse_y > self.y and mouse_y < self.y+self.h

	#draw the button. Call this every frame.
	def draw(self):
		draw_color = self.color
		if self.is_mouseover():
			draw_color = self.color_mouseover
		pygame.draw.rect(screen, draw_color, [self.x, self.y, self.w, self.h])
		text_image = button_font.render(self.text, True, self.text_color)
		text_area = text_image.get_rect()
		text_w = text_area[2]
		text_h = text_area[3]

		screen.blit(text_image, [self.x + self.w/2 - text_w/2, self.y + self.h/2 - text_h/2])
	
	#Make the mouse think. Call this every frame.
	def think(self):
		mouse_clicked = pygame.mouse.get_pressed()[0]

		if mouse_clicked and self.mouse_clicked_last_frame == False and self.is_mouseover():
			self.has_been_clicked = True

		self.mouse_clicked_last_frame = mouse_clicked

#our list of buttons. This is kind of like sprites but for buttons.
buttons = []

#Add one test button.
buttons.append(Button())

#Call this every frame to draw all the buttons
def drawButtons():
	for b in buttons:
		b.draw()

#Call this every frame to think all the buttons
def thinkButtons():
	for b in buttons:
		b.think()

done = False

clock = pygame.time.Clock()

#pygame.mouse.set_visible(0)




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

sprites = [{"type": "player", "x_coord": 250, "y_coord": 450, "health": health,
 "x_width": 20, "y_length": 30, "x_speed": 0, "y_speed": 0, "color": blue}]

background_sprites = [] 
 
def CreateBackground(stage):

	global background_sprites
	background_sprites = []

	i = 100
	
	while i > 0:

		x = randint(0, 490)
		y = randint(20, 490)
		color = bcolors[randint(0,2)]
	
		new_star = {"type": "small", "x_coord": x, "y_coord": y, "x_width": 2, "y_length": 2,
		"y_speed": 0, "color": color}
		
		background_sprites.append(new_star)
		i -= 1
		
	i = 50
	
	while i > 0:
	
		x = randint(0, 500)
		y = randint(20, 500)
		color = bcolors[randint(0,2)]
	
		new_bigstar = {"type": "large", "x_coord": x, "y_coord": y, "x_width": 4, "y_length": 4,
		"y_speed": 1, "color": color}
		
		background_sprites.append(new_bigstar)
		i -= 1
 
	
 
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
		part = {"type": "particle", "x_coord": x, "y_coord": y, "x_speed": x_speed,
		"y_speed": y_speed, "y_length": 2, "x_width": 2, "time": 11, "health": 2, "color": color, "color2": color2}
		sprites.append(part)
		i -= 1


def NextStage(level):

	global stage
	global background_sprites 
	global sprites

	#insert some text or animations for stage increase
	#game over screen probably goes here
	m = 0
	new_stage = True
	for i in sprites:
		if sprites[m]["type"] == "basic_enemy":
			new_stage = False
		m += 1
			
	if new_stage == True and stage < 10:
		
		spawnbasicenemies(level + 2)
		stage += 1
		
	elif stage == 10:
		background_sprites = []
		sprites = []
		screen.fill(black)
		text = font.render(str("Congrats. Level 10 woot!"), True, l_blue)
		screen.blit(text, [150, 200])
		
	elif stage != 10:
		movesprite(sprites)
		drawsprites(sprites)

		
	
	
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
		x_speed = randint(-3, 3)
		y_speed = randint(-3, 3)
		shoot = randint(60, 180)
	
		new_enemy = {"type": "basic_enemy", "x_coord": x, "y_coord": y,
		"x_width": 30, "y_length": 20, "x_speed": x_speed, "y_speed": y_speed,
		"shoot": shoot, "health": 10, "score": 100, "color": color}

		if EnemyCollision(new_enemy) == False:

			sprites.append(new_enemy)
			i -= 1

def firebullet(amount):

	global combo


	x = sprites[0]["x_coord"] + 10
	y = sprites[0]["y_coord"] - 6
	color = colors[randint(0, 8)]
	
	new_bullet = {"type": "p_bullet", "x_coord": x, "y_coord": y, "x_width": 2,
	"y_length": 6, "y_speed": -10, "x_speed": 0, "damage": 5, "health": 1, "color": color}
	sprites.append(new_bullet)
	
	combo += 1
	
def enemyfire(enemy):

	x = enemy["x_coord"] + 15
	y = enemy["y_coord"] + 10
	
	e_bullet = {"type": "e_bullet", "x_coord": x, "y_coord": y, "x_width": 5,
	"y_length": 7, "y_speed": 6, "x_speed": 0, "damage": 5, "health": 1, "color": l_blue}
	sprites.append(e_bullet)
		
def drawsprites(sprites):

	y = 0
	
	for i in background_sprites:
		pygame.draw.rect(screen, background_sprites[y]["color"], [background_sprites[y]["x_coord"],
		background_sprites[y]["y_coord"], background_sprites[y]["x_width"], background_sprites[y]["y_length"]])
		y += 1
	
	x = 0
	for i in sprites:
		pygame.draw.rect(screen, sprites[x]["color"], [sprites[x]["x_coord"], sprites[x]["y_coord"], sprites[x]["x_width"], sprites[x]["y_length"]])
		x += 1
		
def movesprite(sprites):

	global score
	global combo

	#basic physics all objects have, move them by their speed
	i = 0
	while i < len(background_sprites):
		background_sprites[i]["y_coord"] += background_sprites[i]["y_speed"]
		
		if background_sprites[i]["type"] == "small" and background_sprites[i]["y_speed"] == 0:
			if background_sprites[i]["color"] == white:
				background_sprites[i]["y_speed"] = 3
				
			if background_sprites[i]["color"] == pink:
				background_sprites[i]["y_speed"] = 1
				
			if background_sprites[i]["color"] == yellow:
				background_sprites[i]["y_speed"] = 2
				
		elif background_sprites[i]["color"] == yellow and background_sprites[i]["y_speed"] == 3:
			background_sprites[i]["y_speed"] = randint(1, 2)
				
		elif background_sprites[i]["y_coord"] + 2 > 500:
				background_sprites[i]["y_coord"] = 0
				
		i += 1
 	
	
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
			
		elif sprites[i]["type"] == "basic_enemy":
				
			#after about stage 18 boxes get stuck in each other. Need to address that	
				
			result = EnemyCollision(sprites[i])
			
			if result != False:
				sprites[i]["y_speed"] *= -1
				sprites[i]["x_speed"] *= -1
				sprites[result]["y_speed"] *= -1
				sprites[result]["x_speed"] *= -1
			
			if sprites[i]["y_coord"] < 0:
				sprites[i]["y_coord"] = 0
				sprites[i]["y_speed"] *= -1
			
			elif sprites[i]["y_coord"] >= 400:
				sprites[i]["y_coord"] = 400
				sprites[i]["y_speed"] *= -1
				
			elif sprites[i]["x_coord"] < 0:
				sprites[i]["x_coord"] = 0
				sprites[i]["x_speed"] *= -1
		
			elif sprites[i]["x_coord"] + 30 > 500:
				sprites[i]["x_coord"] = 500 - 30
				sprites[i]["x_speed"] *= -1
				
			elif sprites[i]["x_speed"] == 0:
				sprites[i]["x_speed"] = 1
				
			elif sprites[i]["y_speed"] == 0:
				sprites[i]["y_speed"] = 1
				
			sprites[i]["shoot"] -= 1
				
			if sprites[i]["shoot"] == 0:
				enemyfire(sprites[i])
				sprites[i]["shoot"] = 60
		
			elif sprites[i]["health"] <= 0:
			
				score += sprites[i]["score"] * combo
				enemydeath(sprites[i])
				sprites.remove(sprites[i])
				

				
		elif sprites[i]["type"] == "particle":
			if sprites[i]["time"] == 2:
				sprites[i]["color"] = sprites[i]["color2"]
			
			sprites[i]["time"] -= 1	
			
			if sprites[i]["time"] <= 0:
				sprites.remove(sprites[i])
				
		elif sprites[i]["type"] == "player":
			if sprites[i]["x_coord"] < 0:
				sprites[i]["x_coord"] = 0

		
			elif sprites[i]["x_coord"] + 20 > 500:
				sprites[i]["x_coord"] = 500 - 20

		
		i += 1
		
	

CreateBackground(stage)

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
				
	
	
	thinkButtons()
	for button in buttons:
		if button.clicked():
			print "BUTTON WAS CLICKED!!!"
	
	
	screen.fill(black)
	
	text = font.render("Score", True, white)
	screen.blit(text, [0,0])

	text = font.render(str(score), True, white)
	screen.blit(text, [60, 0])
	
	text = font.render("Stage:", True, white)
	screen.blit(text, [420, 0])
	
	text = font.render(str(stage), True, white)
	screen.blit(text, [475, 0])

	drawButtons()
	
	NextStage(stage)
	pygame.display.flip()

	

		
	clock.tick(60)
	
pygame.quit()
