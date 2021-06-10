# File Bullet.py

import random
import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Classes

class Block(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([15,15])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([15,15])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.y = 380
	def update(self):
		pos = pygame.mouse.get_pos()
		self.rect.x = pos[0]

class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([3,15])
		self.image.fill(RED)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y -= 3

# Screening
screen = pygame.display.set_mode([700,400])

# Sprite Groups
all_sprites = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

# Spawning blocks
for i in range(100):
	block = Block()
	block.rect.x = random.randint(0, 685)
	block.rect.y = random.randint(0, 340)

	block_list.add(block)
	all_sprites.add(block)

# Spawning player
player = Player()
all_sprites.add(player)

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			bullet = Bullet()
			bullet.rect.x = player.rect.x
			bullet.rect.y = player.rect.y

			all_sprites.add(bullet)
			bullet_list.add(bullet)

	# Logic Code
	all_sprites.update()
	for bullet in bullet_list:
		blocks_hit = pygame.sprite.spritecollide(bullet, block_list, True)
		for block in blocks_hit:
			bullet_list.remove(bullet)
			all_sprites.remove(bullet)
		if bullet.rect.y < -10:
			bullet_list.remove(bullet)
			all_sprites.remove(bullet)
	# Drawing code
	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()
	clock.tick(30)
pygame.quit()