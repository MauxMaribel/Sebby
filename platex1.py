import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen_width = 800
screen_length = 600

class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		super().__init__()
		
		self.image = pygame.Surface([15, 15])
		self.image.fill(white)
		
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		
		self.change_x = 0
		self.change_y = 0
		self.walls = None
		
	def changespeed(self, x, y):
		self.change_x += x
		self.change_y += y
		
	def update(self):
		self.rect.x += self.change_x
		
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				self.rect.left = block.rect.right
				
		self.rect.y += self.change_y
		
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom
				
class Wall(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height):
		super().__init__()
		
		self.image = pygame.Surface([width, height])
		self.image.fill(green)
		
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_length])

pygame.display.set_caption("Test")

all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list(wall)

player = Player(50, 50)
player.walls = wall_list

all_spite_list.add(player)
clock = pygame.time.Clock()

done = False

while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_d:
				player.changespeed(3,0)
			elif event.key == pygame.K_w:
				player.changespeed(0, -3)
			elif event.key == pygame.K_s:
				player.changespeed(0, 3)
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				player.changespeed(3,0)
			elif event.key == pygame.K_d:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_w:
				player.changespeed(0, 3)
			elif event.key == pygame.K_s:
				player.changespeed(0, -3)
			
	all_sprite_list.update()
			
	screen.fill(black)

	all_sprite_list.draw(screen)
	
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()
			
			
			
			