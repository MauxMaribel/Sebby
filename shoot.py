import pygame
from random import randint

#Make a fireworks function and put at start screen and win screen
#Ask about error with pygame.quit() and how to quit game more naturally
#Create Player Healthbar
#Add Sounds
#Add Boss at stage 9
#Add explosion/shake when player is hit with bullet
#Add Powerups & Transporter ships
#Create dynamic colors for background

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

start = False
dead = False

size = [500, 500]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 15, True, False)

button_font = pygame.font.SysFont('Calibri', 25, True, False)

pygame.display.set_caption("Colortastic explosions")

#This is a Button class. You can create buttons using
#Button() to create a new button object.

class Button:
	x = 70
	y = 300
	w = 120
	h = 80

	text = "test"
	color = l_blue
	color_mouseover = purple
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



def drawButtons():
	for b in buttons:
		b.draw()

#Call this every frame to think all the buttons
def thinkButtons():
	for b in buttons:
		b.think()

done = False

clock = pygame.time.Clock()



startbutton = Button()
startbutton.text = "Start!"
startbutton.color = pink
startbutton.text_color = black
startbutton.color_mouseover = colors[randint(0, 8)]


buttons.append(startbutton)

quitbutton = Button()
quitbutton.text = "Quit"
quitbutton.x = 320
buttons.append(quitbutton)


stage = 0

#bonus for accurate shots. Later show combo on screen
combo = 0

score = 0

x_coord = 250
y_coord = 450

x_speed = 0
y_speed = 0

sprites = [{"type": "player", "x_coord": 250, "y_coord": 450, "health": 100,
 "x_width": 20, "y_length": 30, "x_speed": 0, "y_speed": 0, "color": blue}]

background_sprites = [] 

fireworks = []

def CreateFireworks(amount):

	while amount > 0:
		color = colors[randint(0, 8)]
		x = randint(50, 450)
		x_speed = randint(-1, 1)
		y_speed = randint(-10, -5)
		life = randint(30, 60)
	
		bullet = {"type": "bullet", "x_coord": x, "y_coord": 500, "x_speed": x_speed, "y_speed": y_speed,
		"color": color, "x_width": 4, "y_length": 6, "life": life}
		fireworks.append(bullet)
		amount -= 1
		
	

 
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
		
def NewText(string, color, x, y):
	font = pygame.font.SysFont('Calibri', 15, True, False)
	text = font.render(str(string), True, color)
	screen.blit(text, [x,y])
	
def NewTextLarge(string, color, x, y):
	font = pygame.font.SysFont('Calibri', 30, True, False)
	text = font.render(str(string), True, color)
	screen.blit(text, [x,y])


def NextStage(level):

	global start
	global stage
	global background_sprites 
	global sprites
	global dead
	global score
	global fireworks

	#insert some text or animations for stage increase
	#game over screen probably goes here
	
	if start == False:

		thinkButtons()
		for button in buttons:
			if startbutton.clicked():
				start = True
				fireworks = []
			elif quitbutton.clicked():
				pygame.quit()
				
		if fireworks == []:
			CreateFireworks(randint(10,20))
			
		screen.fill(black)
		movesprite(sprites)
		drawfireworks(fireworks)
		NewTextLarge("Are you ready for some", l_blue, 100, 100)
		NewTextLarge("Colortastic Explosions?", l_blue, 100, 140)
		drawButtons()

		
		
	if start == True:	

		
		if dead == True:
			pygame.mouse.set_visible(1)
			startbutton.text = "Replay"
			sprites = [{"type": "player", "x_coord": 250, "y_coord": 450, "health": 100,
			"x_width": 20, "y_length": 30, "x_speed": 0, "y_speed": 0, "color": blue}]
			background_sprites = []
			screen.fill(black)
			text = font.render(str("You died. Try sucking less."), True, orange)
			screen.blit(text, [150, 200])
			drawButtons()
			thinkButtons()
			for button in buttons:
				if startbutton.clicked():
					stage = 0
					score = 0
					sprites[0]["health"] = 100
					CreateBackground(stage)
					dead = False
					fireworks = []
				elif quitbutton.clicked():
					pygame.quit()
	
		elif dead == False:

		
			pygame.mouse.set_visible(0)
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
				pygame.mouse.set_visible(1)
				background_sprites = []
				sprites = [{"type": "player", "x_coord": 250, "y_coord": 450, "health": 100,
				"x_width": 20, "y_length": 30, "x_speed": 0, "y_speed": 0, "color": pink}]
				
				if fireworks == []:
					CreateFireworks(randint(10, 20))
				
				screen.fill(black)
				movesprite(sprites)
				drawfireworks(fireworks)
				NewTextLarge("Congrats you won~!", orange, 120, 150)
				NewTextLarge("Your Score was", yellow, 170, 200)
				NewTextLarge(str(score), white, 220, 250)
				startbutton.text = "Replay"
				drawButtons()
				thinkButtons()
				for button in buttons:
					if startbutton.clicked():
						stage = 0
						score = 0
						CreateBackground(stage)
						dead = False
						fireworks = []
	
					elif quitbutton.clicked():
						pygame.quit()
				
		
			elif stage != 10:
				text = font.render("Score", True, white)
				screen.blit(text, [0,0])
				
				text = font.render(str(score), True, white)
				screen.blit(text, [60, 0])
			
				text = font.render("Stage:", True, white)
				screen.blit(text, [420, 0])
				
				text = font.render(str(stage), True, white)
				screen.blit(text, [475, 0])

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
	
def playercollision(bullet):

	rect_a = [bullet["x_coord"], bullet["y_coord"], bullet["x_width"], bullet["y_length"]]
	rect_b = [sprites[0]["x_coord"], sprites[0]["y_coord"], sprites[0]["x_width"], sprites[0]["y_length"]]
	
	if DetectCollisions(rect_a, rect_b) == True:
		return True

		
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
		
def drawfireworks(fireworks):

	y = 0
	
	for i in fireworks:
		pygame.draw.rect(screen, fireworks[y]["color"], [fireworks[y]["x_coord"],
		fireworks[y]["y_coord"], fireworks[y]["x_width"], fireworks[y]["y_length"]])
		y += 1
		
def movesprite(sprites):

	global score
	global combo
	global dead
	global fireworks

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
					
		elif sprites[i]["type"] == "e_bullet":
			if sprites[i]["y_coord"] > 500:
				sprites.remove(sprites[i])
				
			elif playercollision(sprites[i]) == True:
				sprites[0]["health"] = sprites[0]["health"] - sprites[i]["damage"]
				sprites.remove(sprites[i])
				sprites[0]["color"] = colors[randint(0,8)]
				
			
		elif sprites[i]["type"] == "basic_enemy":
				
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
			if sprites[i]["health"] <= 0:
				dead = True
		
			elif sprites[i]["x_coord"] < 0:
				sprites[i]["x_coord"] = 0

		
			elif sprites[i]["x_coord"] + 20 > 500:
				sprites[i]["x_coord"] = 500 - 20

		
		i += 1
		
	i = 0
	while i < len(fireworks):

		fireworks[i]["x_coord"] += fireworks[i]["x_speed"]
		fireworks[i]["y_coord"] += fireworks[i]["y_speed"]
		fireworks[i]["life"] -= 1
		
		if fireworks[i]["type"] == "bullet":
			if fireworks[i]["life"] == 0:

				m = 80
				while m > 0:
					x_speed = randint(-3, 3)
					y_speed = randint(-3, 3)
					color = colors[randint(0,8)]
					particle = {"type": "particle", "x_coord": fireworks[i]["x_coord"],
					"y_coord": fireworks[i]["y_coord"], "x_speed": x_speed, "y_speed": y_speed,
					"color": color, "color2": fireworks[i]["color"], "x_width": 2, "y_length": 2, "life": 10}
					fireworks.append(particle)
					m -= 1
				fireworks.remove(fireworks[i])
				
		elif fireworks[i]["type"] == "particle":
			if fireworks[i]["life"] == 5:
				fireworks[i]["color"] = fireworks[i]["color2"]
				
			elif fireworks[i]["life"] == 0:
				fireworks.remove(fireworks[i])
		
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
				
	
	
	
	screen.fill(black)
	
	NextStage(stage)
	pygame.display.flip()

	

		
	clock.tick(60)
	
pygame.quit()
