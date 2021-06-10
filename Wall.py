# File Wall.py

import pygame
pygame.init()

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Classes
# Wall
class Wall(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height,colour):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(colour)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

# Player
class Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface([10,10])
		self.image.fill(RED)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.velocity_x = 0
		self.velocity_y = 0
	def velocity(self,x,y):
		self.velocity_x += x
		self.velocity_y += y

	def update(self,wall):
		self.rect.x += self.velocity_x
		self.rect.y += self.velocity_y
		walls_hit = pygame.sprite.spritecollide(self,wall,False)
		for wall in walls_hit:
			# Moving right
			if self.velocity_x > 0:
				self.rect.right = wall.rect.left
			else:
				self.rect.left = wall.rect.right
			# Up + down
# Sprite groups
all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

# Setting  the screen
width = 700
height = 400
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Walls")

player = Player(340,190)
all_sprites.add(player)
# Creating walls
wall = Wall(30,0,10,700,GREEN)
wall_list.add(wall)
all_sprites.add(wall)
# Main loop
running = True
clock = pygame.time.Clock()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.velocity(-5,0)
			elif event.key == pygame.K_d:
				player.velocity(5,0)
			elif event.key == pygame.K_w:
				player.velocity(0,-5)
			elif event.key == pygame.K_s:
				player.velocity(0,5)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				player.velocity(5,0)
			elif event.key == pygame.K_d:
				player.velocity(-5,0)
			elif event.key == pygame.K_w:
				player.velocity(0,5)
			elif event.key == pygame.K_s:
				player.velocity(0,-5)

	# Drawing Code
	all_sprites.update(wall_list)
	screen.fill(BLACK)
	
	all_sprites.draw(screen)

	pygame.display.flip()
	clock.tick(30)
pygame.quit()