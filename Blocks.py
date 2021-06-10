# File Blocks.py

import random
import pygame
pygame.init()

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,85,0)

# Classes
class Block(pygame.sprite.Sprite):
	def __init__(self,colour,width,height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(colour)
		self.rect = self.image.get_rect()

# Grouping sprites together
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Defining the screen
size = (700,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Blocks")

# Creating entities
for i in range(50):
	i = Block(GREEN,10,10)

	i.rect.x = random.randint(0,(size[0] - 10))
	i.rect.y = random.randint(0,(size[1] - 10))
	block_list.add(i)
	all_sprites_list.add(i)

player = Block(WHITE,5,5)
player.rect.x = 100
player.rect.y = 100
all_sprites_list.add(player)

blocks_killed = pygame.sprite.spritecollide(player, block_list, True)
clock = pygame.time.Clock()
end = False
murdercount = 0
x_velocity = 0
y_velocity = 0
while end == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				x_velocity = -4
			if event.key == pygame.K_d:
				x_velocity = 4
			if event.key == pygame.K_w:
				y_velocity = -4
			if event.key == pygame.K_s:
				y_velocity = 4
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				x_velocity = 0
			if event.key == pygame.K_d:
				x_velocity = 0
			if event.key == pygame.K_w:
				y_velocity = 0
			if event.key == pygame.K_s:
				y_velocity = 0
	
	# Logic code
	player.rect.x += x_velocity
	player.rect.y += y_velocity
	blocks_killed = pygame.sprite.spritecollide(player, block_list, True)
	for i in blocks_killed:
		murdercount +=1
		print(murdercount)
	if player.rect.x < 5 or player.rect.x > 695:
		x_velocity = 0
	if player.rect.y < 5 or player.rect.y > 395:
		y_velocity = 0
	# Drawing code
	screen.fill(BLACK)
	all_sprites_list.draw(screen)
	pygame.display.flip()
	clock.tick(30)
pygame.quit()