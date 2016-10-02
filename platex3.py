import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test Platformer")

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

plat_a = [400, 350, 100, 25]
plat_b = [0, 475, 700, 25]

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 455


def draw_platform(x, y, w, h):
	
	pygame.draw.rect(screen, green, [x, y, w, h])

def playerCollide(rect_a, player):

	#rect_a[0] = plat_xcoord
	#rect_a[1] = plat_ycood
	#rect_a[2] = plat_xwidth
	#rect_a[3] = plat_yheight
	
	#player[0] = player_xcoord
	#player[1] = player_ycoord
	#player[2] = player_xwidth
	#player[3] = player_yheight
	#Boolean Logic: OR auto true unless both False, AND auto false unless both True
	
	#x_apart = plat_xcoord >= player_xcoord + player_xwidth or player_xcoord >= plat_xcoord + plat_xwidth
	#y_apart = plat_ycoord >= player_ycoord + player_yheight or player_ycoord >= plat_ycoord + plat_yheight

	x_apart = rect_a[0] >= player[0] + player[2] or player[0] >= rect_a[0] + rect_a[2]
	y_apart = rect_a[1] >= player[1] + player[3] or player[1] >= rect_a[1] + rect_a[3]
	
	return x_apart == False and y_apart == False


def DetectCollisions(player):

	playerCollide(plat_b, player)
	playerCollide(plat_a, player)
		

	


def MoveHoizontally(amount):


	global x_coord
	if amount > 0:
		direction = 10
	else:
		direction = -10
	x_coord += amount
		
	answer = DetectCollisions(player)
	while answer == False:
		x_coord -= direction
		
		
def MoveVertically(amount):
	global y_coord
	global y_speed
	if amount > 0:
		direction = 1
		
	else:
		direction = -1
	
	y_coord += amount
	
	answer = DetectCollisions(player)
	while answer == False:
		y_coord -= direction

		
		
while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				MoveHoizontally(-10)
				
			elif event.key == pygame.K_d:
				MoveHoizontally(10)
				
			elif event.key == pygame.K_w and y_speed == 0:
				MoveVertically(-30)
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				MoveHoizontally(0)
			
	player = [x_coord, y_coord, 50, 20]
			
	if DetectCollisions(player) == True:
		y_speed = y_speed + 0.3
	else:
		Y_speed = 0

	
	screen.fill(black)
	
	pygame.draw.rect(screen, blue, [x_coord, y_coord, 50, 20])
	
	draw_platform( 400, 350, 100, 25)
	draw_platform( 0, 475, 700, 25)
	


	
	pygame.display.flip()
	
	
	if x_coord < 0:
		x_coord = 0
	elif x_coord + 50 > 700:
		x_coord = 700 - 50
	elif y_coord < 0:
		y_coord = 0
	elif y_coord + 20 > 500:
		y_coord = 500 - 20

	
	clock.tick(60)
	
	
pygame.quit()
		











