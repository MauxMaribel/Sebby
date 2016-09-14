import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test Rectangle")

done = False 
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10




platforms = []

def RectOverLap(rect_a, rect_b):

	x_apart = rect_a[0] > rect_b[0] + rect_b[2] or rect_b[0] > rect_a[0] + rect_a[2]
	y_apart = rect_a[1] > rect_b[1] + rect_b[3] or rect_b[1] > rect_a[1] + rect_a[3]
	
	return x_apart == False and y_apart == False



def draw_rect(screen, x, y):

	pygame.draw.rect(screen, white, [x, y, 50, 20])
	
def draw_platform(screen, x, y, w, h):

	pygame.draw.rect(screen, green, [x, y, w, h])


while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				x_speed = -3
			elif event.key == pygame.K_d:
				x_speed = 3
			elif event.key == pygame.K_w and y_speed == 0:
				y_speed = -10
			
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				x_speed = 0

				


	y_speed = y_speed + 0.3
	x_coord = x_coord + x_speed
	y_coord = y_coord + y_speed
			
	screen.fill(black)
	
	draw_rect(screen, x_coord, y_coord)
	
	draw_platform(screen, 400, 350, 100, 25)
	draw_platform(screen, 0, 475, 700, 25)
	
	player = [x_coord, y_coord, 50, 20]
	plat_a = [400, 350, 100, 25]
	plat_b = [0, 475, 700, 25]
	
	if RectOverLap(plat_a, player) == True:
		
		y_coord = y_coord - y_speed
		y_speed = 0
				
			
	elif RectOverLap(plat_b, player) == True:
		y_speed = 0
		y_coord = 455
		
			
			
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